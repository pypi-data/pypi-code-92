import unittest

import ibm_boto3
from ibm_watson_machine_learning.experiment import AutoAI
from ibm_watson_machine_learning.helpers.connections import DataConnection, S3Location
from ibm_watson_machine_learning.utils.autoai.errors import CannotReadSavedRemoteDataBeforeFit, WMLClientError
from ibm_watson_machine_learning.tests.utils import bucket_exists, create_bucket, is_cp4d
from ibm_watson_machine_learning.tests.autoai.svt.abstract_test_iris_wml_autoai_multiclass_connections import (
                                                AbstractTestAutoAIRemote)

@unittest.skipIf(is_cp4d(), "Not supported on CPD")
class TestAutoAIRemote(AbstractTestAutoAIRemote, unittest.TestCase):
    """
    The test can be run on CLOUD, and CPD
    The test covers:
    - COS connection set-up
    - Saving data `iris.csv` to data assets
    - downloading training data from data assets
    - downloading all generated pipelines to lale pipeline
    - deployment with lale pipeline
    - deployment deletion
    Connection used in test:
    - input: DataAsset pointing to COS.
    - output: ConnectedDataAsset pointing to COS.
    """

    def test_00b_prepare_COS_instance(self):
        TestAutoAIRemote.cos_resource = ibm_boto3.resource(
            service_name="s3",
            endpoint_url=self.cos_endpoint,
            aws_access_key_id=self.cos_credentials['cos_hmac_keys']['access_key_id'],
            aws_secret_access_key=self.cos_credentials['cos_hmac_keys']['secret_access_key']
        )
        # Prepare bucket
        if not bucket_exists(self.cos_resource, self.bucket_name):
            TestAutoAIRemote.bucket_name = create_bucket(self.cos_resource, self.bucket_name)

            self.assertIsNotNone(TestAutoAIRemote.bucket_name)
            self.assertTrue(bucket_exists(self.cos_resource, TestAutoAIRemote.bucket_name))

        self.cos_resource.Bucket(self.bucket_name).upload_file(
            self.data_location,
            self.data_cos_path
        )

    def test_00c_prepare_connection_to_COS(self):
        connection_details = self.wml_client.connections.create({
            'datasource_type': self.wml_client.connections.get_datasource_type_uid_by_name('bluemixcloudobjectstorage'),
            'name': 'Connection to COS for tests',
            'properties': {
                'bucket': self.bucket_name,
                'access_key': self.cos_credentials['cos_hmac_keys']['access_key_id'],
                'secret_key': self.cos_credentials['cos_hmac_keys']['secret_access_key'],
                'iam_url': self.wml_client.service_instance._href_definitions.get_iam_token_url(),
                'url': self.cos_endpoint
            }
        })

        TestAutoAIRemote.connection_id = self.wml_client.connections.get_uid(connection_details)
        self.assertIsInstance(self.connection_id, str)

    def test_00d_prepare_connected_data_asset(self):
        asset_details = self.wml_client.data_assets.store({
            self.wml_client.data_assets.ConfigurationMetaNames.CONNECTION_ID: self.connection_id,
            self.wml_client.data_assets.ConfigurationMetaNames.NAME: "Iris - training asset",
            self.wml_client.data_assets.ConfigurationMetaNames.DATA_CONTENT_NAME: self.data_cos_path
        })

        TestAutoAIRemote.asset_id = self.wml_client.data_assets.get_id(asset_details)
        self.assertIsInstance(self.asset_id, str)

    def test_01_initialize_AutoAI_experiment__pass_credentials__object_initialized(self):
        TestAutoAIRemote.experiment = AutoAI(wml_credentials=self.wml_credentials.copy(),
                                             project_id=self.project_id,
                                             space_id=self.space_id)

        self.assertIsInstance(self.experiment, AutoAI, msg="Experiment is not of type AutoAI.")

    def test_02_DataConnection_setup(self):
        TestAutoAIRemote.data_connection = DataConnection(data_asset_id=self.asset_id)
        TestAutoAIRemote.results_connection = DataConnection(
            connection_asset_id=self.connection_id,
            location=S3Location(
                bucket=self.bucket_name,
                path=self.results_cos_path
            )
        )

        self.assertIsNotNone(obj=TestAutoAIRemote.data_connection)
        self.assertIsNotNone(obj=TestAutoAIRemote.results_connection)

    def test_02a_read_saved_remote_data_before_fit(self):
        self.assertRaises(NotImplementedError, self.data_connection.read)

    def test_29_delete_connection_and_connected_data_asset(self):
        self.wml_client.data_assets.delete(self.asset_id)
        self.wml_client.connections.delete(self.connection_id)

        with self.assertRaises(WMLClientError):
            self.wml_client.data_assets.get_details(self.asset_id)
            self.wml_client.connections.get_details(self.connection_id)


if __name__ == '__main__':
    unittest.main()
