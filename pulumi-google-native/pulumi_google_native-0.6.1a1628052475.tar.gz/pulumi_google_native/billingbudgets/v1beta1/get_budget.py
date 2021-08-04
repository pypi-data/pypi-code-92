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
    'GetBudgetResult',
    'AwaitableGetBudgetResult',
    'get_budget',
]

@pulumi.output_type
class GetBudgetResult:
    def __init__(__self__, all_updates_rule=None, amount=None, budget_filter=None, display_name=None, etag=None, name=None, threshold_rules=None):
        if all_updates_rule and not isinstance(all_updates_rule, dict):
            raise TypeError("Expected argument 'all_updates_rule' to be a dict")
        pulumi.set(__self__, "all_updates_rule", all_updates_rule)
        if amount and not isinstance(amount, dict):
            raise TypeError("Expected argument 'amount' to be a dict")
        pulumi.set(__self__, "amount", amount)
        if budget_filter and not isinstance(budget_filter, dict):
            raise TypeError("Expected argument 'budget_filter' to be a dict")
        pulumi.set(__self__, "budget_filter", budget_filter)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if threshold_rules and not isinstance(threshold_rules, list):
            raise TypeError("Expected argument 'threshold_rules' to be a list")
        pulumi.set(__self__, "threshold_rules", threshold_rules)

    @property
    @pulumi.getter(name="allUpdatesRule")
    def all_updates_rule(self) -> 'outputs.GoogleCloudBillingBudgetsV1beta1AllUpdatesRuleResponse':
        """
        Optional. Rules to apply to notifications sent based on budget spend and thresholds.
        """
        return pulumi.get(self, "all_updates_rule")

    @property
    @pulumi.getter
    def amount(self) -> 'outputs.GoogleCloudBillingBudgetsV1beta1BudgetAmountResponse':
        """
        Budgeted amount.
        """
        return pulumi.get(self, "amount")

    @property
    @pulumi.getter(name="budgetFilter")
    def budget_filter(self) -> 'outputs.GoogleCloudBillingBudgetsV1beta1FilterResponse':
        """
        Optional. Filters that define which resources are used to compute the actual spend against the budget amount, such as projects, services, and the budget's time period, as well as other filters.
        """
        return pulumi.get(self, "budget_filter")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        User data for display name in UI. Validation: <= 60 chars.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Optional. Etag to validate that the object is unchanged for a read-modify-write operation. An empty etag will cause an update to overwrite other changes.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name of the budget. The resource name implies the scope of a budget. Values are of the form `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="thresholdRules")
    def threshold_rules(self) -> Sequence['outputs.GoogleCloudBillingBudgetsV1beta1ThresholdRuleResponse']:
        """
        Optional. Rules that trigger alerts (notifications of thresholds being crossed) when spend exceeds the specified percentages of the budget. Optional for `pubsubTopic` notifications. Required if using email notifications.
        """
        return pulumi.get(self, "threshold_rules")


class AwaitableGetBudgetResult(GetBudgetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBudgetResult(
            all_updates_rule=self.all_updates_rule,
            amount=self.amount,
            budget_filter=self.budget_filter,
            display_name=self.display_name,
            etag=self.etag,
            name=self.name,
            threshold_rules=self.threshold_rules)


def get_budget(billing_account_id: Optional[str] = None,
               budget_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBudgetResult:
    """
    Returns a budget. WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. When reading from the API, you will not see these fields in the return value, though they may have been set in the Cloud Console.
    """
    __args__ = dict()
    __args__['billingAccountId'] = billing_account_id
    __args__['budgetId'] = budget_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:billingbudgets/v1beta1:getBudget', __args__, opts=opts, typ=GetBudgetResult).value

    return AwaitableGetBudgetResult(
        all_updates_rule=__ret__.all_updates_rule,
        amount=__ret__.amount,
        budget_filter=__ret__.budget_filter,
        display_name=__ret__.display_name,
        etag=__ret__.etag,
        name=__ret__.name,
        threshold_rules=__ret__.threshold_rules)
