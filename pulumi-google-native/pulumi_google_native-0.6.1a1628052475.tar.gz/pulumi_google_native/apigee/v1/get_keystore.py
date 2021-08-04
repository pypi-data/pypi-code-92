# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetKeystoreResult',
    'AwaitableGetKeystoreResult',
    'get_keystore',
]

@pulumi.output_type
class GetKeystoreResult:
    def __init__(__self__, aliases=None, name=None):
        if aliases and not isinstance(aliases, list):
            raise TypeError("Expected argument 'aliases' to be a list")
        pulumi.set(__self__, "aliases", aliases)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def aliases(self) -> Sequence[str]:
        """
        Aliases in this keystore.
        """
        return pulumi.get(self, "aliases")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource ID for this keystore. Values must match the regular expression `[\w[:space:]-.]{1,255}`.
        """
        return pulumi.get(self, "name")


class AwaitableGetKeystoreResult(GetKeystoreResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeystoreResult(
            aliases=self.aliases,
            name=self.name)


def get_keystore(environment_id: Optional[str] = None,
                 keystore_id: Optional[str] = None,
                 organization_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeystoreResult:
    """
    Gets a keystore or truststore.
    """
    __args__ = dict()
    __args__['environmentId'] = environment_id
    __args__['keystoreId'] = keystore_id
    __args__['organizationId'] = organization_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:apigee/v1:getKeystore', __args__, opts=opts, typ=GetKeystoreResult).value

    return AwaitableGetKeystoreResult(
        aliases=__ret__.aliases,
        name=__ret__.name)
