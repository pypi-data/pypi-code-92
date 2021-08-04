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
    'GetQueryResult',
    'AwaitableGetQueryResult',
    'get_query',
]

@pulumi.output_type
class GetQueryResult:
    def __init__(__self__, created=None, envgroup_hostname=None, error=None, execution_time=None, name=None, query_params=None, report_definition_id=None, result=None, result_file_size=None, result_rows=None, self=None, state=None, updated=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if envgroup_hostname and not isinstance(envgroup_hostname, str):
            raise TypeError("Expected argument 'envgroup_hostname' to be a str")
        pulumi.set(__self__, "envgroup_hostname", envgroup_hostname)
        if error and not isinstance(error, str):
            raise TypeError("Expected argument 'error' to be a str")
        pulumi.set(__self__, "error", error)
        if execution_time and not isinstance(execution_time, str):
            raise TypeError("Expected argument 'execution_time' to be a str")
        pulumi.set(__self__, "execution_time", execution_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if query_params and not isinstance(query_params, dict):
            raise TypeError("Expected argument 'query_params' to be a dict")
        pulumi.set(__self__, "query_params", query_params)
        if report_definition_id and not isinstance(report_definition_id, str):
            raise TypeError("Expected argument 'report_definition_id' to be a str")
        pulumi.set(__self__, "report_definition_id", report_definition_id)
        if result and not isinstance(result, dict):
            raise TypeError("Expected argument 'result' to be a dict")
        pulumi.set(__self__, "result", result)
        if result_file_size and not isinstance(result_file_size, str):
            raise TypeError("Expected argument 'result_file_size' to be a str")
        pulumi.set(__self__, "result_file_size", result_file_size)
        if result_rows and not isinstance(result_rows, str):
            raise TypeError("Expected argument 'result_rows' to be a str")
        pulumi.set(__self__, "result_rows", result_rows)
        if self and not isinstance(self, str):
            raise TypeError("Expected argument 'self' to be a str")
        pulumi.set(__self__, "self", self)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        pulumi.set(__self__, "updated", updated)

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        Creation time of the query.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="envgroupHostname")
    def envgroup_hostname(self) -> str:
        """
        Hostname is available only when query is executed at host level.
        """
        return pulumi.get(self, "envgroup_hostname")

    @property
    @pulumi.getter
    def error(self) -> str:
        """
        Error is set when query fails.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter(name="executionTime")
    def execution_time(self) -> str:
        """
        ExecutionTime is available only after the query is completed.
        """
        return pulumi.get(self, "execution_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Asynchronous Query Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="queryParams")
    def query_params(self) -> 'outputs.GoogleCloudApigeeV1QueryMetadataResponse':
        """
        Contains information like metrics, dimenstions etc of the AsyncQuery.
        """
        return pulumi.get(self, "query_params")

    @property
    @pulumi.getter(name="reportDefinitionId")
    def report_definition_id(self) -> str:
        """
        Asynchronous Report ID.
        """
        return pulumi.get(self, "report_definition_id")

    @property
    @pulumi.getter
    def result(self) -> 'outputs.GoogleCloudApigeeV1AsyncQueryResultResponse':
        """
        Result is available only after the query is completed.
        """
        return pulumi.get(self, "result")

    @property
    @pulumi.getter(name="resultFileSize")
    def result_file_size(self) -> str:
        """
        ResultFileSize is available only after the query is completed.
        """
        return pulumi.get(self, "result_file_size")

    @property
    @pulumi.getter(name="resultRows")
    def result_rows(self) -> str:
        """
        ResultRows is available only after the query is completed.
        """
        return pulumi.get(self, "result_rows")

    @property
    @pulumi.getter
    def self(self) -> str:
        """
        Self link of the query. Example: `/organizations/myorg/environments/myenv/queries/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` or following format if query is running at host level: `/organizations/myorg/hostQueries/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd`
        """
        return pulumi.get(self, "self")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Query state could be "enqueued", "running", "completed", "failed".
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def updated(self) -> str:
        """
        Last updated timestamp for the query.
        """
        return pulumi.get(self, "updated")


class AwaitableGetQueryResult(GetQueryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQueryResult(
            created=self.created,
            envgroup_hostname=self.envgroup_hostname,
            error=self.error,
            execution_time=self.execution_time,
            name=self.name,
            query_params=self.query_params,
            report_definition_id=self.report_definition_id,
            result=self.result,
            result_file_size=self.result_file_size,
            result_rows=self.result_rows,
            self=self.self,
            state=self.state,
            updated=self.updated)


def get_query(environment_id: Optional[str] = None,
              organization_id: Optional[str] = None,
              query_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQueryResult:
    """
    Get query status If the query is still in progress, the `state` is set to "running" After the query has completed successfully, `state` is set to "completed"
    """
    __args__ = dict()
    __args__['environmentId'] = environment_id
    __args__['organizationId'] = organization_id
    __args__['queryId'] = query_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:apigee/v1:getQuery', __args__, opts=opts, typ=GetQueryResult).value

    return AwaitableGetQueryResult(
        created=__ret__.created,
        envgroup_hostname=__ret__.envgroup_hostname,
        error=__ret__.error,
        execution_time=__ret__.execution_time,
        name=__ret__.name,
        query_params=__ret__.query_params,
        report_definition_id=__ret__.report_definition_id,
        result=__ret__.result,
        result_file_size=__ret__.result_file_size,
        result_rows=__ret__.result_rows,
        self=__ret__.self,
        state=__ret__.state,
        updated=__ret__.updated)
