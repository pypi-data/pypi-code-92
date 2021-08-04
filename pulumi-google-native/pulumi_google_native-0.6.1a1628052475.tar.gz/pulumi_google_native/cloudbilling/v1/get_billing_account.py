# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetBillingAccountResult',
    'AwaitableGetBillingAccountResult',
    'get_billing_account',
]

@pulumi.output_type
class GetBillingAccountResult:
    def __init__(__self__, display_name=None, master_billing_account=None, name=None, open=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if master_billing_account and not isinstance(master_billing_account, str):
            raise TypeError("Expected argument 'master_billing_account' to be a str")
        pulumi.set(__self__, "master_billing_account", master_billing_account)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if open and not isinstance(open, bool):
            raise TypeError("Expected argument 'open' to be a bool")
        pulumi.set(__self__, "open", open)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name given to the billing account, such as `My Billing Account`. This name is displayed in the Google Cloud Console.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="masterBillingAccount")
    def master_billing_account(self) -> str:
        """
        If this account is a [subaccount](https://cloud.google.com/billing/docs/concepts), then this will be the resource name of the parent billing account that it is being resold through. Otherwise this will be empty.
        """
        return pulumi.get(self, "master_billing_account")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF` would be the resource name for billing account `012345-567890-ABCDEF`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def open(self) -> bool:
        """
        True if the billing account is open, and will therefore be charged for any usage on associated projects. False if the billing account is closed, and therefore projects associated with it will be unable to use paid services.
        """
        return pulumi.get(self, "open")


class AwaitableGetBillingAccountResult(GetBillingAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBillingAccountResult(
            display_name=self.display_name,
            master_billing_account=self.master_billing_account,
            name=self.name,
            open=self.open)


def get_billing_account(billing_account_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBillingAccountResult:
    """
    Gets information about a billing account. The current authenticated user must be a [viewer of the billing account](https://cloud.google.com/billing/docs/how-to/billing-access).
    """
    __args__ = dict()
    __args__['billingAccountId'] = billing_account_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:cloudbilling/v1:getBillingAccount', __args__, opts=opts, typ=GetBillingAccountResult).value

    return AwaitableGetBillingAccountResult(
        display_name=__ret__.display_name,
        master_billing_account=__ret__.master_billing_account,
        name=__ret__.name,
        open=__ret__.open)
