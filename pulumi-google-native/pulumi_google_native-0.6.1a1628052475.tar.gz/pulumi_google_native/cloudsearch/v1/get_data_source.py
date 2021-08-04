# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetDataSourceResult',
    'AwaitableGetDataSourceResult',
    'get_data_source',
]

@pulumi.output_type
class GetDataSourceResult:
    def __init__(__self__, disable_modifications=None, disable_serving=None, display_name=None, indexing_service_accounts=None, items_visibility=None, name=None, operation_ids=None, short_name=None):
        if disable_modifications and not isinstance(disable_modifications, bool):
            raise TypeError("Expected argument 'disable_modifications' to be a bool")
        pulumi.set(__self__, "disable_modifications", disable_modifications)
        if disable_serving and not isinstance(disable_serving, bool):
            raise TypeError("Expected argument 'disable_serving' to be a bool")
        pulumi.set(__self__, "disable_serving", disable_serving)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if indexing_service_accounts and not isinstance(indexing_service_accounts, list):
            raise TypeError("Expected argument 'indexing_service_accounts' to be a list")
        pulumi.set(__self__, "indexing_service_accounts", indexing_service_accounts)
        if items_visibility and not isinstance(items_visibility, list):
            raise TypeError("Expected argument 'items_visibility' to be a list")
        pulumi.set(__self__, "items_visibility", items_visibility)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if operation_ids and not isinstance(operation_ids, list):
            raise TypeError("Expected argument 'operation_ids' to be a list")
        pulumi.set(__self__, "operation_ids", operation_ids)
        if short_name and not isinstance(short_name, str):
            raise TypeError("Expected argument 'short_name' to be a str")
        pulumi.set(__self__, "short_name", short_name)

    @property
    @pulumi.getter(name="disableModifications")
    def disable_modifications(self) -> bool:
        """
        If true, sets the datasource to read-only mode. In read-only mode, the Indexing API rejects any requests to index or delete items in this source. Enabling read-only mode does not stop the processing of previously accepted data.
        """
        return pulumi.get(self, "disable_modifications")

    @property
    @pulumi.getter(name="disableServing")
    def disable_serving(self) -> bool:
        """
        Disable serving any search or assist results.
        """
        return pulumi.get(self, "disable_serving")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name of the datasource The maximum length is 300 characters.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="indexingServiceAccounts")
    def indexing_service_accounts(self) -> Sequence[str]:
        """
        List of service accounts that have indexing access.
        """
        return pulumi.get(self, "indexing_service_accounts")

    @property
    @pulumi.getter(name="itemsVisibility")
    def items_visibility(self) -> Sequence['outputs.GSuitePrincipalResponse']:
        """
        This field restricts visibility to items at the datasource level. Items within the datasource are restricted to the union of users and groups included in this field. Note that, this does not ensure access to a specific item, as users need to have ACL permissions on the contained items. This ensures a high level access on the entire datasource, and that the individual items are not shared outside this visibility.
        """
        return pulumi.get(self, "items_visibility")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the datasource resource. Format: datasources/{source_id}. The name is ignored when creating a datasource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationIds")
    def operation_ids(self) -> Sequence[str]:
        """
        IDs of the Long Running Operations (LROs) currently running for this schema.
        """
        return pulumi.get(self, "operation_ids")

    @property
    @pulumi.getter(name="shortName")
    def short_name(self) -> str:
        """
        A short name or alias for the source. This value will be used to match the 'source' operator. For example, if the short name is *<value>* then queries like *source:<value>* will only return results for this source. The value must be unique across all datasources. The value must only contain alphanumeric characters (a-zA-Z0-9). The value cannot start with 'google' and cannot be one of the following: mail, gmail, docs, drive, groups, sites, calendar, hangouts, gplus, keep, people, teams. Its maximum length is 32 characters.
        """
        return pulumi.get(self, "short_name")


class AwaitableGetDataSourceResult(GetDataSourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataSourceResult(
            disable_modifications=self.disable_modifications,
            disable_serving=self.disable_serving,
            display_name=self.display_name,
            indexing_service_accounts=self.indexing_service_accounts,
            items_visibility=self.items_visibility,
            name=self.name,
            operation_ids=self.operation_ids,
            short_name=self.short_name)


def get_data_source(datasource_id: Optional[str] = None,
                    debug_options_enable_debugging: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataSourceResult:
    """
    Gets a datasource. **Note:** This API requires an admin account to execute.
    """
    __args__ = dict()
    __args__['datasourceId'] = datasource_id
    __args__['debugOptionsEnableDebugging'] = debug_options_enable_debugging
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:cloudsearch/v1:getDataSource', __args__, opts=opts, typ=GetDataSourceResult).value

    return AwaitableGetDataSourceResult(
        disable_modifications=__ret__.disable_modifications,
        disable_serving=__ret__.disable_serving,
        display_name=__ret__.display_name,
        indexing_service_accounts=__ret__.indexing_service_accounts,
        items_visibility=__ret__.items_visibility,
        name=__ret__.name,
        operation_ids=__ret__.operation_ids,
        short_name=__ret__.short_name)
