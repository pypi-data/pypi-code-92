# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetVpnTunnelResult',
    'AwaitableGetVpnTunnelResult',
    'get_vpn_tunnel',
]

@pulumi.output_type
class GetVpnTunnelResult:
    def __init__(__self__, creation_timestamp=None, description=None, detailed_status=None, ike_version=None, kind=None, label_fingerprint=None, labels=None, local_traffic_selector=None, name=None, peer_external_gateway=None, peer_external_gateway_interface=None, peer_gcp_gateway=None, peer_ip=None, region=None, remote_traffic_selector=None, router=None, self_link=None, shared_secret=None, shared_secret_hash=None, status=None, target_vpn_gateway=None, vpn_gateway=None, vpn_gateway_interface=None):
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if detailed_status and not isinstance(detailed_status, str):
            raise TypeError("Expected argument 'detailed_status' to be a str")
        pulumi.set(__self__, "detailed_status", detailed_status)
        if ike_version and not isinstance(ike_version, int):
            raise TypeError("Expected argument 'ike_version' to be a int")
        pulumi.set(__self__, "ike_version", ike_version)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if label_fingerprint and not isinstance(label_fingerprint, str):
            raise TypeError("Expected argument 'label_fingerprint' to be a str")
        pulumi.set(__self__, "label_fingerprint", label_fingerprint)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if local_traffic_selector and not isinstance(local_traffic_selector, list):
            raise TypeError("Expected argument 'local_traffic_selector' to be a list")
        pulumi.set(__self__, "local_traffic_selector", local_traffic_selector)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if peer_external_gateway and not isinstance(peer_external_gateway, str):
            raise TypeError("Expected argument 'peer_external_gateway' to be a str")
        pulumi.set(__self__, "peer_external_gateway", peer_external_gateway)
        if peer_external_gateway_interface and not isinstance(peer_external_gateway_interface, int):
            raise TypeError("Expected argument 'peer_external_gateway_interface' to be a int")
        pulumi.set(__self__, "peer_external_gateway_interface", peer_external_gateway_interface)
        if peer_gcp_gateway and not isinstance(peer_gcp_gateway, str):
            raise TypeError("Expected argument 'peer_gcp_gateway' to be a str")
        pulumi.set(__self__, "peer_gcp_gateway", peer_gcp_gateway)
        if peer_ip and not isinstance(peer_ip, str):
            raise TypeError("Expected argument 'peer_ip' to be a str")
        pulumi.set(__self__, "peer_ip", peer_ip)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if remote_traffic_selector and not isinstance(remote_traffic_selector, list):
            raise TypeError("Expected argument 'remote_traffic_selector' to be a list")
        pulumi.set(__self__, "remote_traffic_selector", remote_traffic_selector)
        if router and not isinstance(router, str):
            raise TypeError("Expected argument 'router' to be a str")
        pulumi.set(__self__, "router", router)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if shared_secret and not isinstance(shared_secret, str):
            raise TypeError("Expected argument 'shared_secret' to be a str")
        pulumi.set(__self__, "shared_secret", shared_secret)
        if shared_secret_hash and not isinstance(shared_secret_hash, str):
            raise TypeError("Expected argument 'shared_secret_hash' to be a str")
        pulumi.set(__self__, "shared_secret_hash", shared_secret_hash)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if target_vpn_gateway and not isinstance(target_vpn_gateway, str):
            raise TypeError("Expected argument 'target_vpn_gateway' to be a str")
        pulumi.set(__self__, "target_vpn_gateway", target_vpn_gateway)
        if vpn_gateway and not isinstance(vpn_gateway, str):
            raise TypeError("Expected argument 'vpn_gateway' to be a str")
        pulumi.set(__self__, "vpn_gateway", vpn_gateway)
        if vpn_gateway_interface and not isinstance(vpn_gateway_interface, int):
            raise TypeError("Expected argument 'vpn_gateway_interface' to be a int")
        pulumi.set(__self__, "vpn_gateway_interface", vpn_gateway_interface)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> str:
        """
        Detailed status message for the VPN tunnel.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="ikeVersion")
    def ike_version(self) -> int:
        """
        IKE protocol version to use when establishing the VPN tunnel with the peer VPN gateway. Acceptable IKE versions are 1 or 2. The default version is 2.
        """
        return pulumi.get(self, "ike_version")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of resource. Always compute#vpnTunnel for VPN tunnels.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> str:
        """
        A fingerprint for the labels being applied to this VpnTunnel, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a VpnTunnel.
        """
        return pulumi.get(self, "label_fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Labels for this resource. These can only be added or modified by the setLabels method. Each label key/value pair must comply with RFC1035. Label values may be empty.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="localTrafficSelector")
    def local_traffic_selector(self) -> Sequence[str]:
        """
        Local traffic selector to use when establishing the VPN tunnel with the peer VPN gateway. The value should be a CIDR formatted string, for example: 192.168.0.0/16. The ranges must be disjoint. Only IPv4 is supported.
        """
        return pulumi.get(self, "local_traffic_selector")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerExternalGateway")
    def peer_external_gateway(self) -> str:
        """
        URL of the peer side external VPN gateway to which this VPN tunnel is connected. Provided by the client when the VPN tunnel is created. This field is exclusive with the field peerGcpGateway.
        """
        return pulumi.get(self, "peer_external_gateway")

    @property
    @pulumi.getter(name="peerExternalGatewayInterface")
    def peer_external_gateway_interface(self) -> int:
        """
        The interface ID of the external VPN gateway to which this VPN tunnel is connected. Provided by the client when the VPN tunnel is created.
        """
        return pulumi.get(self, "peer_external_gateway_interface")

    @property
    @pulumi.getter(name="peerGcpGateway")
    def peer_gcp_gateway(self) -> str:
        """
        URL of the peer side HA GCP VPN gateway to which this VPN tunnel is connected. Provided by the client when the VPN tunnel is created. This field can be used when creating highly available VPN from VPC network to VPC network, the field is exclusive with the field peerExternalGateway. If provided, the VPN tunnel will automatically use the same vpnGatewayInterface ID in the peer GCP VPN gateway.
        """
        return pulumi.get(self, "peer_gcp_gateway")

    @property
    @pulumi.getter(name="peerIp")
    def peer_ip(self) -> str:
        """
        IP address of the peer VPN gateway. Only IPv4 is supported.
        """
        return pulumi.get(self, "peer_ip")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        URL of the region where the VPN tunnel resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="remoteTrafficSelector")
    def remote_traffic_selector(self) -> Sequence[str]:
        """
        Remote traffic selectors to use when establishing the VPN tunnel with the peer VPN gateway. The value should be a CIDR formatted string, for example: 192.168.0.0/16. The ranges should be disjoint. Only IPv4 is supported.
        """
        return pulumi.get(self, "remote_traffic_selector")

    @property
    @pulumi.getter
    def router(self) -> str:
        """
        URL of the router resource to be used for dynamic routing.
        """
        return pulumi.get(self, "router")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="sharedSecret")
    def shared_secret(self) -> str:
        """
        Shared secret used to set the secure session between the Cloud VPN gateway and the peer VPN gateway.
        """
        return pulumi.get(self, "shared_secret")

    @property
    @pulumi.getter(name="sharedSecretHash")
    def shared_secret_hash(self) -> str:
        """
        Hash of the shared secret.
        """
        return pulumi.get(self, "shared_secret_hash")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the VPN tunnel, which can be one of the following: - PROVISIONING: Resource is being allocated for the VPN tunnel. - WAITING_FOR_FULL_CONFIG: Waiting to receive all VPN-related configs from the user. Network, TargetVpnGateway, VpnTunnel, ForwardingRule, and Route resources are needed to setup the VPN tunnel. - FIRST_HANDSHAKE: Successful first handshake with the peer VPN. - ESTABLISHED: Secure session is successfully established with the peer VPN. - NETWORK_ERROR: Deprecated, replaced by NO_INCOMING_PACKETS - AUTHORIZATION_ERROR: Auth error (for example, bad shared secret). - NEGOTIATION_FAILURE: Handshake failed. - DEPROVISIONING: Resources are being deallocated for the VPN tunnel. - FAILED: Tunnel creation has failed and the tunnel is not ready to be used. - NO_INCOMING_PACKETS: No incoming packets from peer. - REJECTED: Tunnel configuration was rejected, can be result of being denied access. - ALLOCATING_RESOURCES: Cloud VPN is in the process of allocating all required resources. - STOPPED: Tunnel is stopped due to its Forwarding Rules being deleted for Classic VPN tunnels or the project is in frozen state. - PEER_IDENTITY_MISMATCH: Peer identity does not match peer IP, probably behind NAT. - TS_NARROWING_NOT_ALLOWED: Traffic selector narrowing not allowed for an HA-VPN tunnel. 
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="targetVpnGateway")
    def target_vpn_gateway(self) -> str:
        """
        URL of the Target VPN gateway with which this VPN tunnel is associated. Provided by the client when the VPN tunnel is created.
        """
        return pulumi.get(self, "target_vpn_gateway")

    @property
    @pulumi.getter(name="vpnGateway")
    def vpn_gateway(self) -> str:
        """
        URL of the VPN gateway with which this VPN tunnel is associated. Provided by the client when the VPN tunnel is created. This must be used (instead of target_vpn_gateway) if a High Availability VPN gateway resource is created.
        """
        return pulumi.get(self, "vpn_gateway")

    @property
    @pulumi.getter(name="vpnGatewayInterface")
    def vpn_gateway_interface(self) -> int:
        """
        The interface ID of the VPN gateway with which this VPN tunnel is associated.
        """
        return pulumi.get(self, "vpn_gateway_interface")


class AwaitableGetVpnTunnelResult(GetVpnTunnelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpnTunnelResult(
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            detailed_status=self.detailed_status,
            ike_version=self.ike_version,
            kind=self.kind,
            label_fingerprint=self.label_fingerprint,
            labels=self.labels,
            local_traffic_selector=self.local_traffic_selector,
            name=self.name,
            peer_external_gateway=self.peer_external_gateway,
            peer_external_gateway_interface=self.peer_external_gateway_interface,
            peer_gcp_gateway=self.peer_gcp_gateway,
            peer_ip=self.peer_ip,
            region=self.region,
            remote_traffic_selector=self.remote_traffic_selector,
            router=self.router,
            self_link=self.self_link,
            shared_secret=self.shared_secret,
            shared_secret_hash=self.shared_secret_hash,
            status=self.status,
            target_vpn_gateway=self.target_vpn_gateway,
            vpn_gateway=self.vpn_gateway,
            vpn_gateway_interface=self.vpn_gateway_interface)


def get_vpn_tunnel(project: Optional[str] = None,
                   region: Optional[str] = None,
                   vpn_tunnel: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpnTunnelResult:
    """
    Returns the specified VpnTunnel resource. Gets a list of available VPN tunnels by making a list() request.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['region'] = region
    __args__['vpnTunnel'] = vpn_tunnel
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/alpha:getVpnTunnel', __args__, opts=opts, typ=GetVpnTunnelResult).value

    return AwaitableGetVpnTunnelResult(
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        detailed_status=__ret__.detailed_status,
        ike_version=__ret__.ike_version,
        kind=__ret__.kind,
        label_fingerprint=__ret__.label_fingerprint,
        labels=__ret__.labels,
        local_traffic_selector=__ret__.local_traffic_selector,
        name=__ret__.name,
        peer_external_gateway=__ret__.peer_external_gateway,
        peer_external_gateway_interface=__ret__.peer_external_gateway_interface,
        peer_gcp_gateway=__ret__.peer_gcp_gateway,
        peer_ip=__ret__.peer_ip,
        region=__ret__.region,
        remote_traffic_selector=__ret__.remote_traffic_selector,
        router=__ret__.router,
        self_link=__ret__.self_link,
        shared_secret=__ret__.shared_secret,
        shared_secret_hash=__ret__.shared_secret_hash,
        status=__ret__.status,
        target_vpn_gateway=__ret__.target_vpn_gateway,
        vpn_gateway=__ret__.vpn_gateway,
        vpn_gateway_interface=__ret__.vpn_gateway_interface)
