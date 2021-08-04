#  Copyright (c) 2021 Food-X Technologies
#
#  This file is part of foodx_devops_tools.
#
#  You should have received a copy of the MIT License along with
#  foodx_devops_tools. If not, see <https://opensource.org/licenses/MIT>.

"""Azure resource group utilities."""

import asyncio
import json
import logging
import pathlib
import re

from foodx_devops_tools.utility import run_async_command

from .model import AzureSubscriptionConfiguration

log = logging.getLogger(__name__)

AZURE_GROUP_ID_PATTERN = (
    r"^/subscriptions/"
    r"(?P<subscription_id>[0-9a-z\-]+)"
    r"/resourceGroups/"
    r"(?P<group_name>[A-Za-z0-9\-_]+)"
)
AZURE_GROUP_MATCH = re.compile(AZURE_GROUP_ID_PATTERN)


class ResourceGroupError(Exception):
    """Problem occurred with resource group related actions."""


async def check_exists(
    resource_group_name: str, subscription: AzureSubscriptionConfiguration
) -> dict:
    """
    Determine if a resource group exists in the specified subscription.

    Assume authentication has already occurred such that subsequent ``az``
    CLI commands will succeed.

    Args:
        resource_group_name: Name of resource group to find
        subscription: Subscription to search for resource group

    Returns:
        Query result data on success. Empty dictionary otherwise.
    Raises:
        ResourceGroupError: If any error occurs preventing the search from
                            completing.
    """
    try:
        this_command = [
            "az",
            "group",
            "list",
            "--subscription",
            subscription.subscription_id,
        ]
        log.debug("{0}".format(str(this_command)))
        result = await run_async_command(this_command)
        log.debug(
            "resource group existence check stdout, {0}".format(result.out)
        )
        log.debug(
            "resource group existence check stderr, {0}".format(result.error)
        )

        result_data = json.loads(result.out)
        log.debug("{0}".format(str(result_data)))
        group_result = dict()
        for this_group in result_data:
            this_match = AZURE_GROUP_MATCH.match(this_group["id"])
            if (
                this_match
                and this_match.group("group_name") == resource_group_name
            ):
                group_result = this_group.copy()
                log.debug("group exists, {0}".format(str(group_result)))

        return group_result
    except asyncio.CancelledError:
        # should almost always let async cancelled exceptions propagate.
        raise
    except Exception as e:
        raise ResourceGroupError(
            "Problem acquiring resource group data, {0}".format(
                resource_group_name
            )
        ) from e


async def create(
    resource_group_name: str,
    location: str,
    subscription: AzureSubscriptionConfiguration,
) -> None:
    """
    Idempotent creation of an Azure resource group.

    Args:
        resource_group_name: Name of resource group to create.
        location: Azure location in which to create the resource group.
        subscription: Azure subscription identity for the resource group.
    """
    group_data = await check_exists(resource_group_name, subscription)
    if not group_data:
        result = await run_async_command(
            [
                "az",
                "group",
                "create",
                "--resource-group",
                resource_group_name,
                "--location",
                location,
            ]
        )
        log.debug("resource group creation stdout, {0}".format(result.out))
        log.debug("resource group creation stderr, {0}".format(result.error))


async def delete(
    resource_group_name: str,
    subscription: AzureSubscriptionConfiguration,
) -> None:
    """
    Delete an Azure resource group.

    Args:
        resource_group_name: Name of resource group to create.
        subscription: Azure subscription identity for the resource group.
    """
    group_data = await check_exists(resource_group_name, subscription)
    if group_data:
        log.info(
            "deleting resource group, {0}, {1}".format(
                resource_group_name, subscription.subscription_id
            )
        )
        result = await run_async_command(
            [
                "az",
                "group",
                "delete",
                "--resource-group",
                resource_group_name,
                "--yes",
            ]
        )
        log.debug("resource group deletion stdout, {0}".format(result.out))
        log.debug("resource group deletion stderr, {0}".format(result.error))
    else:
        log.info(
            "no delete resource group as it does not exist, {0}, {1}".format(
                resource_group_name, subscription.subscription_id
            )
        )


async def deploy(
    resource_group_name: str,
    arm_template_path: pathlib.Path,
    arm_parameters_path: pathlib.Path,
    location: str,
    subscription: AzureSubscriptionConfiguration,
) -> None:
    """
    Deploy resource to a resource group.

    The resources are defined in ARM template JSON or bicep files, per Azure
    CLI utility.

    Args:
        resource_group_name: Resource group name
        arm_template_path: Path to ARM template deployment file.
        arm_parameters_path: Path to ARM template deployment parameters file.
        location: Azure location in which to deploy resource group.
        subscription: Target subscription/tenant for deployment.
    """
    await create(resource_group_name, location, subscription)
    this_command = [
        "az",
        "deployment",
        "group",
        "create",
        "--resource-group",
        resource_group_name,
        "--parameters",
        "{0}".format(arm_parameters_path),
        "--template-file",
        str(arm_template_path),
    ]
    result = await run_async_command(this_command)
    log.debug("resource group deployment stdout, {0}".format(result.out))
    log.debug("resource group deployment stderr, {0}".format(result.error))
