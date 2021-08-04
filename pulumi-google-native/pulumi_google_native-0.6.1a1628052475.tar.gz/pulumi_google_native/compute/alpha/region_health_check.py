# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['RegionHealthCheckArgs', 'RegionHealthCheck']

@pulumi.input_type
class RegionHealthCheckArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 check_interval_sec: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 grpc_health_check: Optional[pulumi.Input['GRPCHealthCheckArgs']] = None,
                 healthy_threshold: Optional[pulumi.Input[int]] = None,
                 http2_health_check: Optional[pulumi.Input['HTTP2HealthCheckArgs']] = None,
                 http_health_check: Optional[pulumi.Input['HTTPHealthCheckArgs']] = None,
                 https_health_check: Optional[pulumi.Input['HTTPSHealthCheckArgs']] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 log_config: Optional[pulumi.Input['HealthCheckLogConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 ssl_health_check: Optional[pulumi.Input['SSLHealthCheckArgs']] = None,
                 tcp_health_check: Optional[pulumi.Input['TCPHealthCheckArgs']] = None,
                 timeout_sec: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input['RegionHealthCheckType']] = None,
                 udp_health_check: Optional[pulumi.Input['UDPHealthCheckArgs']] = None,
                 unhealthy_threshold: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a RegionHealthCheck resource.
        :param pulumi.Input[int] check_interval_sec: How often (in seconds) to send a health check. The default value is 5 seconds.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[int] healthy_threshold: A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.
        :param pulumi.Input[str] kind: Type of the resource.
        :param pulumi.Input['HealthCheckLogConfigArgs'] log_config: Configure logging on this health check.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash.
        :param pulumi.Input[int] timeout_sec: How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.
        :param pulumi.Input['RegionHealthCheckType'] type: Specifies the type of the healthCheck, either TCP, SSL, HTTP, HTTPS or HTTP2. If not specified, the default is TCP. Exactly one of the protocol-specific health check field must be specified, which must match type field.
        :param pulumi.Input[int] unhealthy_threshold: A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.
        """
        pulumi.set(__self__, "region", region)
        if check_interval_sec is not None:
            pulumi.set(__self__, "check_interval_sec", check_interval_sec)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if grpc_health_check is not None:
            pulumi.set(__self__, "grpc_health_check", grpc_health_check)
        if healthy_threshold is not None:
            pulumi.set(__self__, "healthy_threshold", healthy_threshold)
        if http2_health_check is not None:
            pulumi.set(__self__, "http2_health_check", http2_health_check)
        if http_health_check is not None:
            pulumi.set(__self__, "http_health_check", http_health_check)
        if https_health_check is not None:
            pulumi.set(__self__, "https_health_check", https_health_check)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if log_config is not None:
            pulumi.set(__self__, "log_config", log_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if ssl_health_check is not None:
            pulumi.set(__self__, "ssl_health_check", ssl_health_check)
        if tcp_health_check is not None:
            pulumi.set(__self__, "tcp_health_check", tcp_health_check)
        if timeout_sec is not None:
            pulumi.set(__self__, "timeout_sec", timeout_sec)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if udp_health_check is not None:
            pulumi.set(__self__, "udp_health_check", udp_health_check)
        if unhealthy_threshold is not None:
            pulumi.set(__self__, "unhealthy_threshold", unhealthy_threshold)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="checkIntervalSec")
    def check_interval_sec(self) -> Optional[pulumi.Input[int]]:
        """
        How often (in seconds) to send a health check. The default value is 5 seconds.
        """
        return pulumi.get(self, "check_interval_sec")

    @check_interval_sec.setter
    def check_interval_sec(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "check_interval_sec", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="grpcHealthCheck")
    def grpc_health_check(self) -> Optional[pulumi.Input['GRPCHealthCheckArgs']]:
        return pulumi.get(self, "grpc_health_check")

    @grpc_health_check.setter
    def grpc_health_check(self, value: Optional[pulumi.Input['GRPCHealthCheckArgs']]):
        pulumi.set(self, "grpc_health_check", value)

    @property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> Optional[pulumi.Input[int]]:
        """
        A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.
        """
        return pulumi.get(self, "healthy_threshold")

    @healthy_threshold.setter
    def healthy_threshold(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "healthy_threshold", value)

    @property
    @pulumi.getter(name="http2HealthCheck")
    def http2_health_check(self) -> Optional[pulumi.Input['HTTP2HealthCheckArgs']]:
        return pulumi.get(self, "http2_health_check")

    @http2_health_check.setter
    def http2_health_check(self, value: Optional[pulumi.Input['HTTP2HealthCheckArgs']]):
        pulumi.set(self, "http2_health_check", value)

    @property
    @pulumi.getter(name="httpHealthCheck")
    def http_health_check(self) -> Optional[pulumi.Input['HTTPHealthCheckArgs']]:
        return pulumi.get(self, "http_health_check")

    @http_health_check.setter
    def http_health_check(self, value: Optional[pulumi.Input['HTTPHealthCheckArgs']]):
        pulumi.set(self, "http_health_check", value)

    @property
    @pulumi.getter(name="httpsHealthCheck")
    def https_health_check(self) -> Optional[pulumi.Input['HTTPSHealthCheckArgs']]:
        return pulumi.get(self, "https_health_check")

    @https_health_check.setter
    def https_health_check(self, value: Optional[pulumi.Input['HTTPSHealthCheckArgs']]):
        pulumi.set(self, "https_health_check", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input['HealthCheckLogConfigArgs']]:
        """
        Configure logging on this health check.
        """
        return pulumi.get(self, "log_config")

    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input['HealthCheckLogConfigArgs']]):
        pulumi.set(self, "log_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)

    @property
    @pulumi.getter(name="sslHealthCheck")
    def ssl_health_check(self) -> Optional[pulumi.Input['SSLHealthCheckArgs']]:
        return pulumi.get(self, "ssl_health_check")

    @ssl_health_check.setter
    def ssl_health_check(self, value: Optional[pulumi.Input['SSLHealthCheckArgs']]):
        pulumi.set(self, "ssl_health_check", value)

    @property
    @pulumi.getter(name="tcpHealthCheck")
    def tcp_health_check(self) -> Optional[pulumi.Input['TCPHealthCheckArgs']]:
        return pulumi.get(self, "tcp_health_check")

    @tcp_health_check.setter
    def tcp_health_check(self, value: Optional[pulumi.Input['TCPHealthCheckArgs']]):
        pulumi.set(self, "tcp_health_check", value)

    @property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> Optional[pulumi.Input[int]]:
        """
        How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.
        """
        return pulumi.get(self, "timeout_sec")

    @timeout_sec.setter
    def timeout_sec(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout_sec", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['RegionHealthCheckType']]:
        """
        Specifies the type of the healthCheck, either TCP, SSL, HTTP, HTTPS or HTTP2. If not specified, the default is TCP. Exactly one of the protocol-specific health check field must be specified, which must match type field.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['RegionHealthCheckType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="udpHealthCheck")
    def udp_health_check(self) -> Optional[pulumi.Input['UDPHealthCheckArgs']]:
        return pulumi.get(self, "udp_health_check")

    @udp_health_check.setter
    def udp_health_check(self, value: Optional[pulumi.Input['UDPHealthCheckArgs']]):
        pulumi.set(self, "udp_health_check", value)

    @property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[pulumi.Input[int]]:
        """
        A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.
        """
        return pulumi.get(self, "unhealthy_threshold")

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "unhealthy_threshold", value)


class RegionHealthCheck(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 check_interval_sec: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 grpc_health_check: Optional[pulumi.Input[pulumi.InputType['GRPCHealthCheckArgs']]] = None,
                 healthy_threshold: Optional[pulumi.Input[int]] = None,
                 http2_health_check: Optional[pulumi.Input[pulumi.InputType['HTTP2HealthCheckArgs']]] = None,
                 http_health_check: Optional[pulumi.Input[pulumi.InputType['HTTPHealthCheckArgs']]] = None,
                 https_health_check: Optional[pulumi.Input[pulumi.InputType['HTTPSHealthCheckArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 log_config: Optional[pulumi.Input[pulumi.InputType['HealthCheckLogConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 ssl_health_check: Optional[pulumi.Input[pulumi.InputType['SSLHealthCheckArgs']]] = None,
                 tcp_health_check: Optional[pulumi.Input[pulumi.InputType['TCPHealthCheckArgs']]] = None,
                 timeout_sec: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input['RegionHealthCheckType']] = None,
                 udp_health_check: Optional[pulumi.Input[pulumi.InputType['UDPHealthCheckArgs']]] = None,
                 unhealthy_threshold: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Creates a HealthCheck resource in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] check_interval_sec: How often (in seconds) to send a health check. The default value is 5 seconds.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[int] healthy_threshold: A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.
        :param pulumi.Input[str] kind: Type of the resource.
        :param pulumi.Input[pulumi.InputType['HealthCheckLogConfigArgs']] log_config: Configure logging on this health check.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash.
        :param pulumi.Input[int] timeout_sec: How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.
        :param pulumi.Input['RegionHealthCheckType'] type: Specifies the type of the healthCheck, either TCP, SSL, HTTP, HTTPS or HTTP2. If not specified, the default is TCP. Exactly one of the protocol-specific health check field must be specified, which must match type field.
        :param pulumi.Input[int] unhealthy_threshold: A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegionHealthCheckArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a HealthCheck resource in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param RegionHealthCheckArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegionHealthCheckArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 check_interval_sec: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 grpc_health_check: Optional[pulumi.Input[pulumi.InputType['GRPCHealthCheckArgs']]] = None,
                 healthy_threshold: Optional[pulumi.Input[int]] = None,
                 http2_health_check: Optional[pulumi.Input[pulumi.InputType['HTTP2HealthCheckArgs']]] = None,
                 http_health_check: Optional[pulumi.Input[pulumi.InputType['HTTPHealthCheckArgs']]] = None,
                 https_health_check: Optional[pulumi.Input[pulumi.InputType['HTTPSHealthCheckArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 log_config: Optional[pulumi.Input[pulumi.InputType['HealthCheckLogConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 ssl_health_check: Optional[pulumi.Input[pulumi.InputType['SSLHealthCheckArgs']]] = None,
                 tcp_health_check: Optional[pulumi.Input[pulumi.InputType['TCPHealthCheckArgs']]] = None,
                 timeout_sec: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input['RegionHealthCheckType']] = None,
                 udp_health_check: Optional[pulumi.Input[pulumi.InputType['UDPHealthCheckArgs']]] = None,
                 unhealthy_threshold: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegionHealthCheckArgs.__new__(RegionHealthCheckArgs)

            __props__.__dict__["check_interval_sec"] = check_interval_sec
            __props__.__dict__["description"] = description
            __props__.__dict__["grpc_health_check"] = grpc_health_check
            __props__.__dict__["healthy_threshold"] = healthy_threshold
            __props__.__dict__["http2_health_check"] = http2_health_check
            __props__.__dict__["http_health_check"] = http_health_check
            __props__.__dict__["https_health_check"] = https_health_check
            __props__.__dict__["kind"] = kind
            __props__.__dict__["log_config"] = log_config
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["ssl_health_check"] = ssl_health_check
            __props__.__dict__["tcp_health_check"] = tcp_health_check
            __props__.__dict__["timeout_sec"] = timeout_sec
            __props__.__dict__["type"] = type
            __props__.__dict__["udp_health_check"] = udp_health_check
            __props__.__dict__["unhealthy_threshold"] = unhealthy_threshold
            __props__.__dict__["creation_timestamp"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["self_link_with_id"] = None
        super(RegionHealthCheck, __self__).__init__(
            'google-native:compute/alpha:RegionHealthCheck',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RegionHealthCheck':
        """
        Get an existing RegionHealthCheck resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RegionHealthCheckArgs.__new__(RegionHealthCheckArgs)

        __props__.__dict__["check_interval_sec"] = None
        __props__.__dict__["creation_timestamp"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["grpc_health_check"] = None
        __props__.__dict__["healthy_threshold"] = None
        __props__.__dict__["http2_health_check"] = None
        __props__.__dict__["http_health_check"] = None
        __props__.__dict__["https_health_check"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["log_config"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["self_link_with_id"] = None
        __props__.__dict__["ssl_health_check"] = None
        __props__.__dict__["tcp_health_check"] = None
        __props__.__dict__["timeout_sec"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["udp_health_check"] = None
        __props__.__dict__["unhealthy_threshold"] = None
        return RegionHealthCheck(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="checkIntervalSec")
    def check_interval_sec(self) -> pulumi.Output[int]:
        """
        How often (in seconds) to send a health check. The default value is 5 seconds.
        """
        return pulumi.get(self, "check_interval_sec")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in 3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="grpcHealthCheck")
    def grpc_health_check(self) -> pulumi.Output['outputs.GRPCHealthCheckResponse']:
        return pulumi.get(self, "grpc_health_check")

    @property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> pulumi.Output[int]:
        """
        A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.
        """
        return pulumi.get(self, "healthy_threshold")

    @property
    @pulumi.getter(name="http2HealthCheck")
    def http2_health_check(self) -> pulumi.Output['outputs.HTTP2HealthCheckResponse']:
        return pulumi.get(self, "http2_health_check")

    @property
    @pulumi.getter(name="httpHealthCheck")
    def http_health_check(self) -> pulumi.Output['outputs.HTTPHealthCheckResponse']:
        return pulumi.get(self, "http_health_check")

    @property
    @pulumi.getter(name="httpsHealthCheck")
    def https_health_check(self) -> pulumi.Output['outputs.HTTPSHealthCheckResponse']:
        return pulumi.get(self, "https_health_check")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output['outputs.HealthCheckLogConfigResponse']:
        """
        Configure logging on this health check.
        """
        return pulumi.get(self, "log_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. For example, a name that is 1-63 characters long, matches the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`, and otherwise complies with RFC1035. This regular expression describes a name where the first character is a lowercase letter, and all following characters are a dash, lowercase letter, or digit, except the last character, which isn't a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Region where the health check resides. Not applicable to global health checks.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> pulumi.Output[str]:
        """
        Server-defined URL for this resource with the resource id.
        """
        return pulumi.get(self, "self_link_with_id")

    @property
    @pulumi.getter(name="sslHealthCheck")
    def ssl_health_check(self) -> pulumi.Output['outputs.SSLHealthCheckResponse']:
        return pulumi.get(self, "ssl_health_check")

    @property
    @pulumi.getter(name="tcpHealthCheck")
    def tcp_health_check(self) -> pulumi.Output['outputs.TCPHealthCheckResponse']:
        return pulumi.get(self, "tcp_health_check")

    @property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> pulumi.Output[int]:
        """
        How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec.
        """
        return pulumi.get(self, "timeout_sec")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Specifies the type of the healthCheck, either TCP, SSL, HTTP, HTTPS or HTTP2. If not specified, the default is TCP. Exactly one of the protocol-specific health check field must be specified, which must match type field.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="udpHealthCheck")
    def udp_health_check(self) -> pulumi.Output['outputs.UDPHealthCheckResponse']:
        return pulumi.get(self, "udp_health_check")

    @property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> pulumi.Output[int]:
        """
        A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.
        """
        return pulumi.get(self, "unhealthy_threshold")

