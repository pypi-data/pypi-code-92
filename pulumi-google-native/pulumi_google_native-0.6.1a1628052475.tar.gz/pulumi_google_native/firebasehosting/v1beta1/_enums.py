# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DomainRedirectType',
]


class DomainRedirectType(str, Enum):
    """
    Required. The redirect status code.
    """
    REDIRECT_TYPE_UNSPECIFIED = "REDIRECT_TYPE_UNSPECIFIED"
    """The default redirect type; should not be intentionlly used."""
    MOVED_PERMANENTLY = "MOVED_PERMANENTLY"
    """The redirect will respond with an HTTP status code of `301 Moved Permanently`."""
