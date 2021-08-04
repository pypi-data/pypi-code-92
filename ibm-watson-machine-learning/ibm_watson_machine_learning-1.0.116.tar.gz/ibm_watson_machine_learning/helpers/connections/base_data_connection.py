# (C) Copyright IBM Corp. 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = [
    "BaseDataConnection"
]

import io
import json
import os

from abc import ABC, abstractmethod
from typing import Union, Tuple, TYPE_CHECKING
from warnings import warn

import requests
from pandas import concat, DataFrame

from ibm_watson_machine_learning.utils.autoai.utils import try_load_dataset, try_load_tar_gz
from ibm_watson_machine_learning.utils.autoai.enums import DataConnectionTypes
from ibm_watson_machine_learning.utils.autoai.errors import CannotReadSavedRemoteDataBeforeFit, WrongAssetType
from ibm_watson_machine_learning.wml_client_error import ApiRequestFailure, WMLClientError

if TYPE_CHECKING:
    from ibm_boto3 import resource


class BaseDataConnection(ABC):
    """
    Base class for  DataConnection.
    """

    def __init__(self):

        self.type = None
        self.connection = None
        self.location = None
        self.auto_pipeline_params = None
        self._wml_client = None
        self._run_id = None
        self._obm = None
        self._obm_cos_path = None
        self.id = None

    @abstractmethod
    def _to_dict(self) -> dict:
        """Convert DataConnection object to dictionary representation."""
        pass

    @classmethod
    @abstractmethod
    def _from_dict(cls, _dict: dict) -> 'BaseDataConnection':
        """Create a DataConnection object from dictionary."""
        pass

    @abstractmethod
    def read(self, with_holdout_split: bool = False) -> Union['DataFrame', Tuple['DataFrame', 'DataFrame']]:
        """Download dataset stored in remote data storage."""
        pass

    @abstractmethod
    def write(self, data: Union[str, 'DataFrame'], remote_name: str) -> None:
        """Upload file to a remote data storage."""
        pass

    def _fill_experiment_parameters(self, prediction_type: str, prediction_column: str, holdout_size: float,
                                    csv_separator: str = ',', excel_sheet: Union[str, int] = 0,
                                    encoding: str = 'utf-8') -> None:
        """
        To be able to recreate a holdout split, this method need to be called.
        """
        self.auto_pipeline_params = {
            'prediction_type': prediction_type,
            'prediction_column': prediction_column,
            'holdout_size': holdout_size,
            'csv_separator': csv_separator,
            'excel_sheet': excel_sheet,
            'encoding': encoding
        }

    def _download_obm_data_from_cos(self, cos_client: 'resource') -> 'DataFrame':
        """Download preprocessed OBM data. COS version."""

        if '//' in self._obm_cos_path:  # sometimes there is an additional slash, need to replace it
            self._obm_cos_path = self._obm_cos_path.replace('//', '/')

        # note: fetch all OBM file part names
        cos_summary = cos_client.Bucket(self.location.bucket).objects.filter(Prefix=self._obm_cos_path)
        file_names = [file_name.key for file_name in cos_summary]

        # note: if path does not exist, try to find in different one
        if not file_names:
            cos_summary = cos_client.Bucket(self.location.bucket).objects.filter(
                Prefix=self._obm_cos_path.split('./')[-1])
            file_names = [file_name.key for file_name in cos_summary]
            # --- end note
        # --- end note

        # TODO: this can be done simultaneously (multithreading / multiprocessing)
        # note: download all data parts and concatenate them into one output
        parts = []
        for file_name in file_names:
            file = cos_client.Object(self.location.bucket, file_name).get()
            buffer = io.BytesIO(file['Body'].read())
            parts.append(try_load_dataset(buffer=buffer))

        data = concat(parts)
        # --- end note
        return data

    def _download_obm_json(self) -> dict:
        """Download obm.json log."""
        if self._obm:
            if self._obm_cos_path:
                path = self._obm_cos_path.rsplit('features', 1)[0] + 'obm.json'
            else:
                path = f"{self.location.path}/{self._run_id}/data/obm/obm.json"
            data = self._download_json_file(path)
            return data
        else:
            raise Exception("OBM function called when not OBM scenario.")

    def _download_json_file(self, path) -> dict:
        """Download json file."""
        json_content = {}

        if '//' in path:  # sometimes there is an additional slash, need to replace it
            path = path.replace('//', '/')

        # TODO: remove S3 implementation
        if self.type == DataConnectionTypes.S3:
            warn(message="S3 DataConnection is deprecated! Please use data_asset_id instead.")

            cos_client = self._init_cos_client()

            try:
                file = cos_client.Object(self.location.bucket, path).get()
                content = file["Body"].read()
                json_content = json.loads(content.decode('utf-8'))
            except Exception as cos_access_exception:
                raise ConnectionError(
                    f"Unable to access data object in cloud object storage with credentials supplied. "
                    f"Error: {cos_access_exception}")
        elif self.type == DataConnectionTypes.FS:
            json_url = self._wml_client.service_instance._href_definitions.get_wsd_model_attachment_href() + f"/auto_ml/{path.split('/auto_ml/')[-1]}"

            with requests.get(json_url, params=self._wml_client._params(), headers=self._wml_client._get_headers(),
                              stream=True, verify=False) as file_response:
                if file_response.status_code != 200:
                    raise ApiRequestFailure(u'Failure during {}.'.format("downloading json"), file_response)

                downloaded_asset = file_response.content
                buffer = io.BytesIO(downloaded_asset)
                json_content = json.loads(buffer.getvalue().decode('utf-8'))

        elif self.type == DataConnectionTypes.CA:
            if self._check_if_connection_asset_is_s3():
                cos_client = self._init_cos_client()

                try:
                    file = cos_client.Object(self.location.bucket, path).get()
                    content = file["Body"].read()
                    json_content = json.loads(content.decode('utf-8'))

                except Exception as cos_access_exception:
                    raise ConnectionError(
                        f"Unable to access data object in cloud object storage with credentials supplied. "
                        f"Error: {cos_access_exception}")

            else:
                raise NotImplementedError(f"Unsupported connection type: {self.type}. "
                                          f"Datasource type is not supported. "
                                          f"Supported type is: bluemixcloudobjectstorage")

        else:
            raise NotImplementedError(f"Unsupported connection type: {self.type}")

        return json_content

    def _check_if_connection_asset_is_s3(self) -> bool:
        try:
            if self.type == 'data_asset':
                if self.connection is not None:
                    items = self.connection.href.split('/')

                else:
                    items = self.location.href.split('/')
                _id = items[-1].split('?')[0]

                if self._wml_client is not None:
                    data_asset_details = self._wml_client.data_assets.get_details(_id)

                    attachment_id = data_asset_details['metadata']['attachment_id']
                    if not self._wml_client.ICP and not self._wml_client.WSD:
                        response = requests.get(
                            self._wml_client.service_instance._href_definitions.get_attachment_href(_id, attachment_id),
                            params=self._wml_client.data_assets._client._params(),
                            headers=self._wml_client.data_assets._client._get_headers())
                    else:
                        response = requests.get(
                            self._wml_client.service_instance._href_definitions.get_attachment_href(_id, attachment_id),
                            params=self._wml_client.data_assets._client._params(),
                            headers=self._wml_client.data_assets._client._get_headers(),
                            verify=False)

                    if response.status_code == 200:
                        attachment_details = response.json()
                        if 'connection_id' not in attachment_details:
                            return False

                        connection_details = self._wml_client.connections.get_details(
                            attachment_details['connection_id'])

                    else:
                        raise WMLClientError("Failed while downloading the attachment " + attachment_id)

                else:
                    try:
                        from project_lib import Project
                        project = Project.access()

                        # note: Check if asset is located directly in the project files
                        #       If yes it is not a connected data.
                        #       [Prevents unnecessary logging].
                        if any(file['asset_id'] == _id for file in project.get_files()):
                            return False
                        # --- end note

                        try:
                            connection_details = project.get_connected_data(_id)

                        except RuntimeError:  # when data asset is normal not s3 or database
                            return False

                        attachment_details = {'connection_path': connection_details.get('datapath')}

                    except ModuleNotFoundError:
                        raise NotImplementedError(f"This functionality can be run only on Watson Studio.")

            elif self.type == 'connection_asset':
                if self._wml_client is not None:
                    connection_details = self._wml_client.connections.get_details(self.connection.id)

                else:
                    try:
                        from project_lib import Project
                        project = Project.access()
                        connection_details = project.get_connection(self.connection.id)

                    except ModuleNotFoundError:
                        raise NotImplementedError(f"This functionality can be run only on Watson Studio.")

            elif self.type == 'container':
                if self._wml_client is not None:
                    if self._wml_client.default_space_id is not None:
                        details = self._wml_client.spaces.get_details(self._wml_client.default_space_id)

                    else:
                        project_url = self._wml_client.service_instance._href_definitions.get_project_href(
                            self._wml_client.default_project_id)
                        if self._wml_client.ICP:
                            response = requests.get(
                                project_url,
                                headers=self._wml_client._get_headers(),
                                verify=False
                            )

                        else:
                            response = requests.get(
                                    project_url,
                                    headers=self._wml_client._get_headers()
                                )

                        details = response.json()

                    properties = details['entity']['storage']['properties']
                    properties.update(details['entity']['storage']['properties']['credentials']['editor'])
                    properties['url'] = properties['endpoint_url']
                    properties['access_key'] = properties.get('access_key_id')
                    properties['secret_key'] = properties.get('secret_access_key')

                    connection_details = {
                        'entity': {
                            'datasource_type': 'bluemixcloudobjectstorage',
                            'properties': properties
                        }
                    }

                else:
                    try:
                        from project_lib import Project
                        token = os.environ.get('USER_ACCESS_TOKEN')

                        if token is None:
                            raise NotImplementedError(
                                f"""To succesfully read the training data used in AutoAI experiment, you need to provide the project token.
                            **To insert the project token to your notebook:**
                                Click the More icon on your notebook toolbar and then click Insert project token.
                                Run the inserted code cell.
                            Note:
                            If you are told in a message that no project token exists, click the link in the message to be redirected to the project's Settings page where you can create a project token.
                            **To create a project token:**
                                Click New token in the Access tokens section on the Settings page of your project.
                                Enter a name, select Editor role for the project, and create a token.
                                Go back to your notebook, click the More icon on the notebook toolbar and then click Insert project token.
                                Run the inserted code cell."""
                            )

                        token = token.split('Bearer ')[-1]

                        _project = Project(project_id=os.environ.get('PROJECT_ID'),
                                           project_access_token=token)

                        details = _project.get_storage_metadata()

                        properties = details['properties']
                        properties.update(properties['credentials']['editor'])
                        properties['url'] = properties['endpoint_url']
                        properties['access_key'] = properties.get('access_key_id')
                        properties['secret_key'] = properties.get('secret_access_key')

                        connection_details = {
                            'entity': {
                                'datasource_type': 'bluemixcloudobjectstorage',
                                'properties': properties
                            }
                        }

                    except ModuleNotFoundError:
                        raise NotImplementedError(f"This functionality can be run only on Watson Studio.")

            elif self.type == 's3' or self.type == 'fs':
                return False

            else:
                raise WrongAssetType(asset_type=self.type)

            # Note: Check with project libs if connection points to S3
            if self._wml_client is not None:
                datasource_type = connection_details['entity']['datasource_type']
                datasource_type_id_ibm_cos = self._wml_client.connections.get_datasource_type_uid_by_name(
                    'bluemixcloudobjectstorage')
                datasource_type_id_aws_cos = self._wml_client.connections.get_datasource_type_uid_by_name(
                    'cloudobjectstorage')

                if (datasource_type == datasource_type_id_ibm_cos or datasource_type == datasource_type_id_aws_cos or
                        datasource_type == 'bluemixcloudobjectstorage' or datasource_type == 'cloudobjectstorage'):
                    cos_type = True

                else:
                    cos_type = False

            elif self.type == 'container':
                cos_type = True

            elif 'url' in connection_details:
                cos_type = True
                connection_details['entity'] = {'properties': connection_details}

            else:
                cos_type = False
            # --- end note

            if cos_type:
                if 'cos_hmac_keys' in str(connection_details['entity']['properties']):
                    creds = json.loads(connection_details['entity']['properties']['credentials'])
                    connection_details['entity']['properties']['access_key'] = creds['cos_hmac_keys']['access_key_id']
                    connection_details['entity']['properties']['secret_key'] = creds['cos_hmac_keys'][
                        'secret_access_key']

                if self.connection is None:
                    from .connections import S3Connection
                    self.connection = S3Connection(
                        endpoint_url=connection_details['entity']['properties'].get('url'),
                        access_key_id=connection_details['entity']['properties'].get('access_key'),
                        secret_access_key=connection_details['entity']['properties'].get('secret_key')
                    )

                else:
                    self.connection.secret_access_key = connection_details['entity']['properties'].get('secret_key')
                    self.connection.access_key_id = connection_details['entity']['properties'].get('access_key')
                    self.connection.endpoint_url = connection_details['entity']['properties'].get('url')

                if self.type == 'container':
                    self.location.bucket = connection_details['entity']['properties']['bucket_name']

                if self.type == 'data_asset':
                    try:
                        self.location.bucket = attachment_details['connection_path'].split('/')[1]
                        self.location.path = attachment_details['connection_path'].split('/')[2]

                    except IndexError:
                        self.location.bucket = connection_details['entity']['properties']['bucket']
                        self.location.path = attachment_details['connection_path']

                return True

            else:
                return False

        except Exception as e:
            if os.environ.get('USER_ACCESS_TOKEN') is None:
                raise e

            else:
                return False  # if we are in WS, ignore this check even if there was some error

    def _download_indices_from_cos(self, cos_client: 'resource', location_path) -> 'DataFrame':
        """Download indices for this connection. COS version"""

        try:
            file = cos_client.Object(self.location.bucket,
                                     location_path).get()
        except:
            file = list(cos_client.Bucket(self.location.bucket).objects.filter(
                Prefix=location_path))[0].get()

        buffer = io.BytesIO(file['Body'].read())
        data = try_load_tar_gz(buffer=buffer,
                               separator=self.auto_pipeline_params.get('csv_separator', ','),
                               encoding=self.auto_pipeline_params.get('encoding', 'utf-8')
                               )

        return data

    def _download_data_from_cos(self, cos_client: 'resource') -> 'DataFrame':
        """Download training data for this connection. COS version"""
        location = self.location.file_name if hasattr(self.location, "file_name") else self.location.path
        try:
            file = cos_client.Object(self.location.bucket,
                                     location).get()
        except:
            file = list(cos_client.Bucket(self.location.bucket).objects.filter(
                Prefix=location))[0].get()

        buffer = io.BytesIO(file['Body'].read())
        data = try_load_dataset(buffer=buffer,
                                sheet_name=self.auto_pipeline_params.get('excel_sheet', 0),
                                separator=self.auto_pipeline_params.get('csv_separator', ','),
                                encoding=self.auto_pipeline_params.get('encoding', 'utf-8')
                                )

        return data

    def _download_training_data_from_data_asset_storage(self) -> 'DataFrame':
        """Download training data for this connection. Data Storage."""

        if self._wml_client is not None:
            # note: as we need to load a data into the memory,
            # we are using pure requests and helpers from the WML client
            asset_id = self.location.href.split('?')[0].split('/')[-1]

            # note: download data asset details
            asset_response = requests.get(
                self._wml_client.service_instance._href_definitions.get_data_asset_href(asset_id),
                params=self._wml_client._params(),
                headers=self._wml_client._get_headers(),
                verify=False)

            asset_details = self._wml_client.data_assets._handle_response(200, u'get assets', asset_response)

            # note: read the csv url
            if 'handle' in asset_details['attachments'][0]:
                attachment_url = asset_details['attachments'][0]['handle']['key']

                # note: make the whole url pointing out the csv
                artifact_content_url = (
                    f"{self._wml_client.service_instance._href_definitions.get_wsd_model_attachment_href()}"
                    f"{attachment_url}")

                # note: stream the whole CSV file
                csv_response = requests.get(artifact_content_url,
                                            params=self._wml_client._params(),
                                            headers=self._wml_client._get_headers(),
                                            stream=True,
                                            verify=False)

                if csv_response.status_code != 200:
                    raise ApiRequestFailure(u'Failure during {}.'.format("downloading model"), csv_response)

                downloaded_asset = csv_response.content

                # note: read the csv/xlsx file from the memory directly into the pandas DataFrame
                buffer = io.BytesIO(downloaded_asset)
                data = try_load_dataset(buffer=buffer,
                                        sheet_name=self.auto_pipeline_params.get('excel_sheet', 0),
                                        separator=self.auto_pipeline_params.get('csv_separator', ','),
                                        encoding=self.auto_pipeline_params.get('encoding', 'utf-8')
                                        )

                return data
            else:
                # NFS scenario
                connection_id = asset_details['attachments'][0]['connection_id']
                connection_path = asset_details['attachments'][0]['connection_path']

                return self._download_data_from_nfs_connection_using_id_and_path(connection_id, connection_path)

        else:
            try:
                from project_lib import Project
                project = Project.access()

            except ModuleNotFoundError:
                raise NotImplementedError(f"This functionality can be run only on Watson Studio.")

            asset_id = self.location.href.split('?')[0].split('/')[-1]
            assets_list = project.get_assets()

            data_asset_name = None
            for asset in assets_list:
                if asset['asset_id'] == asset_id:
                    data_asset_name = asset['name']

            if data_asset_name is None:
                raise FileNotFoundError(f"Cannot find data asset with id: {asset_id}")

            buffer = project.get_file(data_asset_name)
            data = try_load_dataset(buffer=buffer,
                                    sheet_name=self.auto_pipeline_params.get('excel_sheet', 0),
                                    separator=self.auto_pipeline_params.get('csv_separator', ','),
                                    encoding=self.auto_pipeline_params.get('encoding', 'utf-8')
                                    )

            return data

    def _download_training_data_from_file_system(self) -> 'DataFrame':
        """Download training data for this connection. File system version."""

        try:
            url = self._wml_client.service_instance._href_definitions.get_wsd_model_attachment_href() + f"/{self.location.path.split('/assets/')[-1]}"
            # note: stream the whole CSV file
            csv_response = requests.get(url,
                                        params=self._wml_client._params(),
                                        headers=self._wml_client._get_headers(),
                                        stream=True,
                                        verify=False)

            if csv_response.status_code != 200:
                raise ApiRequestFailure(u'Failure during {}.'.format("downloading model"), csv_response)

            downloaded_asset = csv_response.content
            # note: read the csv/xlsx file from the memory directly into the pandas DataFrame
            buffer = io.BytesIO(downloaded_asset)
            data = try_load_dataset(buffer=buffer,
                                    sheet_name=self.auto_pipeline_params.get('excel_sheet', 0),
                                    separator=self.auto_pipeline_params.get('csv_separator', ','),
                                    encoding=self.auto_pipeline_params.get('encoding', 'utf-8')
                                    )
        except (ApiRequestFailure, AttributeError):
            with open(self.location.path, 'rb') as data_buffer:
                data = try_load_dataset(buffer=data_buffer,
                                        sheet_name=self.auto_pipeline_params.get('excel_sheet', 0),
                                        separator=self.auto_pipeline_params.get('csv_separator', ','),
                                        encoding=self.auto_pipeline_params.get('encoding', 'utf-8')
                                        )

        return data

    def _download_indices_from_file_system(self, location_path: str) -> 'DataFrame':
        """Download indices for this connection. File system version."""

        try:
            url = self._wml_client.service_instance._href_definitions.get_wsd_model_attachment_href() + f"/{location_path.split('/assets/')[-1]}"
            # note: stream the whole CSV file
            csv_response = requests.get(url,
                                        params=self._wml_client._params(),
                                        headers=self._wml_client._get_headers(),
                                        stream=True,
                                        verify=False)

            if csv_response.status_code != 200:
                raise ApiRequestFailure(u'Failure during {}.'.format("downloading model"), csv_response)

            downloaded_asset = csv_response.content
            # note: read the csv/xlsx file from the memory directly into the pandas DataFrame
            buffer = io.BytesIO(downloaded_asset)
            data = try_load_dataset(buffer=buffer,
                                    sheet_name=self.auto_pipeline_params.get('excel_sheet', 0),
                                    separator=self.auto_pipeline_params.get('csv_separator', ','),
                                    encoding=self.auto_pipeline_params.get('encoding', 'utf-8')
                                    )
        except (ApiRequestFailure, AttributeError):
            with open(location_path, 'rb') as data_buffer:
                data = try_load_tar_gz(buffer=data_buffer,
                                       separator=self.auto_pipeline_params.get('csv_separator', ','),
                                       encoding=self.auto_pipeline_params.get('encoding', 'utf-8')
                                       )

        return data

    def _download_obm_data_from_file_system(self) -> 'DataFrame':
        """Download preprocessed OBM data. FS version."""

        # note: fetch all OBM file part names
        url = self._wml_client.service_instance._href_definitions.get_wsd_model_attachment_href() + f"/auto_ml/{self.location.path.split('/auto_ml/')[-1]}/{self._run_id}/data/obm/features"
        params = self._wml_client._params()
        params['flat'] = "true"

        response = requests.get(url,
                                params=params,
                                headers=self._wml_client._get_headers(),
                                verify=False)

        if response.status_code != 200:
            raise ApiRequestFailure(u'Failure during {}.'.format("getting files information"), response)

        file_names = [e['path'].split('/')[-1] for e in response.json()['resources'] if
                      e['type'] == 'file' and e['path'].split('/')[-1].startswith('part')]

        # TODO: this can be done simultaneously (multithreading / multiprocessing)
        # note: download all data parts and concatenate them into one output
        parts = []
        for file_name in file_names:
            csv_response = requests.get(url + '/' + file_name,
                                        params=self._wml_client._params(),
                                        headers=self._wml_client._get_headers(),
                                        stream=True,
                                        verify=False)

            if csv_response.status_code != 200:
                raise ApiRequestFailure(u'Failure during {}.'.format("downloading model"), csv_response)

            downloaded_asset = csv_response.content
            # note: read the csv/xlsx file from the memory directly into the pandas DataFrame
            buffer = io.BytesIO(downloaded_asset)
            parts.append(try_load_dataset(buffer=buffer))

        data = concat(parts)
        # --- end note
        return data

    def _download_data_from_nfs_connection(self) -> 'DataFrame':
        """Download training data for this connection. NFS."""

        # note: as we need to load a data into the memory,
        # we are using pure requests and helpers from the WML client
        data_path = self.location.path
        connection_id = self.connection.asset_id

        return self._download_data_from_nfs_connection_using_id_and_path(connection_id, data_path)

    def _download_data_from_nfs_connection_using_id_and_path(self, connection_id, connection_path) -> 'DataFrame':
        """Download training data for this connection. NFS."""

        # it means that it is on ICP env and it is before fit, so let's throw error
        if not self._wml_client:
            raise CannotReadSavedRemoteDataBeforeFit()

        # Note: workaround with volumes API as connections API changes data format
        connection_details = self._wml_client.connections.get_details(connection_id)

        href = self._wml_client.volumes._href_definitions.volume_upload_href(
            connection_details['entity']['properties']['volume'])
        full_href = f"{href[:-1]}{connection_path}"

        csv_response = requests.get(full_href,
                                    headers=self._wml_client._get_headers(),
                                    verify=False,
                                    stream=True)

        # Note: if file is written in directory we need to create different href for download
        if csv_response.status_code != 200:
            path_parts = connection_path.split('/')
            full_href = f"{href[:-1]}{'/'.join(path_parts[:-1])}%2F{path_parts[-1]}"

            csv_response = requests.get(full_href,
                                        headers=self._wml_client._get_headers(),
                                        verify=False,
                                        stream=True)

            if csv_response.status_code != 200:
                raise ApiRequestFailure(u'Failure during {}.'.format("downloading data"), csv_response)

        downloaded_asset = csv_response.content
        # note: read the csv/xlsx file from the memory directly into the pandas DataFrame
        buffer = io.BytesIO(downloaded_asset)
        data = try_load_dataset(buffer=buffer,
                                sheet_name=self.auto_pipeline_params.get('excel_sheet', 0),
                                separator=self.auto_pipeline_params.get('csv_separator', ','),
                                encoding=self.auto_pipeline_params.get('encoding', 'utf-8')
                                )

        return data
