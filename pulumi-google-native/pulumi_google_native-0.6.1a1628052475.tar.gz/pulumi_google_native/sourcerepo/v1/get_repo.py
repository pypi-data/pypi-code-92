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
    'GetRepoResult',
    'AwaitableGetRepoResult',
    'get_repo',
]

@pulumi.output_type
class GetRepoResult:
    def __init__(__self__, mirror_config=None, name=None, pubsub_configs=None, size=None, url=None):
        if mirror_config and not isinstance(mirror_config, dict):
            raise TypeError("Expected argument 'mirror_config' to be a dict")
        pulumi.set(__self__, "mirror_config", mirror_config)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pubsub_configs and not isinstance(pubsub_configs, dict):
            raise TypeError("Expected argument 'pubsub_configs' to be a dict")
        pulumi.set(__self__, "pubsub_configs", pubsub_configs)
        if size and not isinstance(size, str):
            raise TypeError("Expected argument 'size' to be a str")
        pulumi.set(__self__, "size", size)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="mirrorConfig")
    def mirror_config(self) -> 'outputs.MirrorConfigResponse':
        """
        How this repository mirrors a repository managed by another service. Read-only field.
        """
        return pulumi.get(self, "mirror_config")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name of the repository, of the form `projects//repos/`. The repo name may contain slashes. eg, `projects/myproject/repos/name/with/slash`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pubsubConfigs")
    def pubsub_configs(self) -> Mapping[str, str]:
        """
        How this repository publishes a change in the repository through Cloud Pub/Sub. Keyed by the topic names.
        """
        return pulumi.get(self, "pubsub_configs")

    @property
    @pulumi.getter
    def size(self) -> str:
        """
        The disk usage of the repo, in bytes. Read-only field. Size is only returned by GetRepo.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        URL to clone the repository from Google Cloud Source Repositories. Read-only field.
        """
        return pulumi.get(self, "url")


class AwaitableGetRepoResult(GetRepoResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRepoResult(
            mirror_config=self.mirror_config,
            name=self.name,
            pubsub_configs=self.pubsub_configs,
            size=self.size,
            url=self.url)


def get_repo(project: Optional[str] = None,
             repo_id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRepoResult:
    """
    Returns information about a repo.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['repoId'] = repo_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:sourcerepo/v1:getRepo', __args__, opts=opts, typ=GetRepoResult).value

    return AwaitableGetRepoResult(
        mirror_config=__ret__.mirror_config,
        name=__ret__.name,
        pubsub_configs=__ret__.pubsub_configs,
        size=__ret__.size,
        url=__ret__.url)
