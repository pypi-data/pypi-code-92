"""DNS module."""
import logging

from typing import cast, List, Optional, Sequence, Union

from dns import resolver, reversename, rrset
from dns.exception import DNSException
from dns.name import Name

from wmflib.constants import PUBLIC_AUTHDNS
from wmflib.exceptions import WmflibError


logger = logging.getLogger(__name__)


class DnsError(WmflibError):
    """Custom exception class for errors of the Dns class."""


class DnsNotFound(DnsError):
    """Custom exception class to indicate the record was not found.

    One or more resource records exist for this domain but there isn’t a record matching the resource record type.
    """


class Dns:
    """Class to interact with the DNS."""

    def __init__(self, *, nameserver_addresses: Optional[Sequence] = None, port: Optional[int] = None) -> None:
        """Initialize the instance.

        Arguments:
            nameserver_addresses (Sequence, optional): the nameserveres address to use, if not set uses the OS
                configuration.
            port (int, optional): the port the ``nameserver_addresses`` nameserveres is listening to, if different from
                the default 53. This applies only if a nameserveres is explicitelyes specified.

        """
        if nameserver_addresses is not None:
            self._resolver = resolver.Resolver(configure=False)
            if port is not None:
                self._resolver.port = port
            self._resolver.nameservers = nameserver_addresses
        else:
            self._resolver = resolver.Resolver()

    def resolve_ipv4(self, name: str) -> List[str]:
        """Perform a DNS lookup for an A record for the given name.

        Arguments:
            name (str): the name to resolve.

        Returns:
            list: the list of IPv4 addresses as strings returned by the DNS response.

        """
        return self._resolve_addresses(name, 'A')

    def resolve_ipv6(self, name: str) -> List[str]:
        """Perform a DNS lookup for an AAAA record for the given name.

        Arguments:
            name (str): the name to resolve.

        Returns:
            list: the list of IPv6 addresses as strings returned by the DNS response.

        """
        return self._resolve_addresses(name, 'AAAA')

    def resolve_ips(self, name: str) -> List[str]:
        """Perform a DNS lookup for A and AAAA records for the given name.

        Arguments:
            name (str): the name to resolve.

        Returns:
            list: the list of IPv4 and IPv6 addresses as strings returned by the DNS response.

        Raises:
            wmflib.dns.DnsNotFound: when no address is found.

        """
        addresses = []
        for func in ('resolve_ipv4', 'resolve_ipv6'):
            try:
                addresses += getattr(self, func)(name)
            except DnsNotFound:
                pass  # Allow single stack answers

        if not addresses:
            raise DnsNotFound('Record A or AAAA not found for {name}'.format(name=name))

        return addresses

    def resolve_ptr(self, address: str) -> List[str]:
        """Perform a DNS lookup for PTR record for the given address.

        Arguments:
            address (str): the IPv4 or IPv6 address to resolve.

        Returns:
            list: the list of absolute target PTR records as strings, without the trailing dot.

        """
        response = self.resolve(reversename.from_address(address), 'PTR')
        return self._parse_targets(cast(rrset.RRset, response.rrset))

    def resolve_cname(self, name: str) -> str:
        """Perform a DNS lookup for CNAME record for the given name.

        Arguments:
            name (str): the name to resolve.

        Returns:
            str: the absolute target name for this CNAME, without the trailing dot.

        """
        targets = self._parse_targets(cast(rrset.RRset, self.resolve(name, 'CNAME').rrset))
        if len(targets) != 1:
            raise DnsError('Found multiple CNAMEs target for {name}: {targets}'.format(name=name, targets=targets))

        return targets[0]

    def resolve(self, qname: Union[str, Name], record_type: str) -> resolver.Answer:
        """Perform a DNS lookup for the given qname and record type.

        Arguments:
            qname (str): the name or address to resolve.
            record_type (str): the DNS record type to lookup for, like 'A', 'AAAA', 'PTR', etc.

        Returns:
            dns.resolver.Answer: the DNS response.

        Raises:
            wmflib.dns.DnsNotFound: if there are no records for the given record type but the qname has records for
                different record type(s).
            wmflib.dns.DnsError: on generic error.

        """
        try:
            response = self._resolver.query(qname, record_type)
            logger.debug('Resolved %s record for %s: %s', record_type, qname, response.rrset)
        except (resolver.NoAnswer, resolver.NXDOMAIN) as e:
            raise DnsNotFound('Record {record_type} not found for {qname}'.format(
                record_type=record_type, qname=qname)) from e
        except DNSException as e:
            raise DnsError('Unable to resolve {record_type} record for {qname}'.format(
                record_type=record_type, qname=qname)) from e

        return response

    def _resolve_addresses(self, name: str, record_type: str) -> List[str]:
        """Extract and return all the matching addresses for the given name and record type.

        Arguments:
            name (str): the name to resolve.
            record_type (str): the DNS record type to lookup for, like 'A' and 'AAAA'.

        Returns:
            list: the list of IPv4 or IPv6 addresses as strings returned by the DNS response.

        """
        return [rdata.address for rdata in cast(rrset.RRset, self.resolve(name, record_type).rrset)]

    @staticmethod
    def _parse_targets(response_set: rrset.RRset) -> List[str]:
        """Extract and return all the matching names from the given rrset without the trailing dot.

        Arguments:
            response_set (dns.rrset.RRset): the RRset to parse.

        Returns:
            list: the list of absolute target record names as strings without the trailing dot.

        Raises:
            wmflib.dns.DnsError: if a relative record is found.

        """
        targets = []
        for rdata in response_set:
            target = rdata.target.to_text()
            if target[-1] != '.':
                raise DnsError('Unsupported relative target {target} found'.format(target=target))

            targets.append(target[:-1])

        return targets


class PublicAuthDns(Dns):
    """Class to interact with the DNS using the wikimedia foundation authoritative servers."""

    def __init__(self) -> None:
        """Initialize the instance."""
        super().__init__(nameserver_addresses=PUBLIC_AUTHDNS)
