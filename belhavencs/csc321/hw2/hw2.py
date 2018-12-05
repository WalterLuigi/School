#!/usr/bin/python

import ipaddress
import netifaces
import netaddr


def get_interfaces():
    """Return a list of all the interfaces on this host

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (list) List of interfaces for this host
    """

    return netifaces.interfaces()

def get_mac(interface: str):
    """For the given interface string, return the MAC address as a
    string

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (str) MAC address
    """

    addrs = netifaces.ifaddresses(interface)
    mac = str.split(str(addrs[netifaces.AF_LINK]))
    mac = mac[1]
    mac = mac[1:-3]
    return mac

def get_ips(interface: str):
    """For the given interface string, return a dictionary with
    the IPv4 and IPv6 address objects for that interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Address('192.168.65.48'),
       'v6': ipaddress.IPv6Address('fe80::14e1:8686:e720:57a')}
    """

    ipdict = {}
    addrs = netifaces.ifaddresses(interface)
    ipv4 = str.split(str(addrs[netifaces.AF_INET]))
    ipv4 = ipv4[1]
    ipv4 = ipv4[1:-2]
    ipv4 = ipaddress.IPv4Address(ipv4)
    ipv6 = str.split(str(addrs[netifaces.AF_INET6]))
    ipv6 = ipv6[1]
    ipv6 = ipv6[1:-2]
    ipv6 = ipaddress.IPv6Address(ipv6)
    ipdict['v4'] = ipv4
    ipdict['v6'] = ipv6
    return ipdict

def get_netmask(interface: str):
    """For the given interface string, return a dictionary with the
    IPv4 and IPv6 netmask objects (as IPv4/v6Address objects) for that
    interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Address('255.255.255.0'),
       'v6': ipaddress.IPv6Address('ffff:ffff:ffff:ffff::')}
    """

    netmaskdict = {}
    addrs = netifaces.ifaddresses(interface)
    ipv4 = str.split(str(addrs[netifaces.AF_INET]))
    ipv4 = ipv4[3]
    ipv4 = ipv4[1:-2]
    ipv4 = ipaddress.IPv4Address(ipv4)
    ipv6 = str.split(str(addrs[netifaces.AF_INET6]))
    ipv6 = ipv6[3]
    ipv6 = ipv6[1:-6]
    ipv6 = ipaddress.IPv6Address(ipv6)
    netmaskdict['v4'] = ipv4
    netmaskdict['v6'] = ipv6
    return netmaskdict

def get_network(interface: str):
    """For the given interface string, return a dictionary with
    the IPv4 and IPv6 network objects for that interface

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (dict) Dictionary with the following form
      {'v4': ipaddress.IPv4Network('192.168.65.0/24'),
       'v6': ipaddress.IPv6Network('fe80::/64')}
    """

    networkdict = {}
    addrs = netifaces.ifaddresses(interface)
    ipv4 = str.split(str(addrs[netifaces.AF_INET]))
    v4netmask = ipv4[3]
    v4netmask = v4netmask[1:-5]
    cidr4 = netaddr.IPAddress(v4netmask).netmask_bits()
    ipv4 = ipv4[1]
    ipv4 = ipv4[1:-2]
    ipv4net = netaddr.IPNetwork(ipv4 + "/" + str(cidr4))
    ipv4net = ipv4net.cidr
    ipv6 = str.split(str(addrs[netifaces.AF_INET6]))
    v6netmask = ipv6[3]
    v6netmask = v6netmask[1:-5]
    cidr6 = netaddr.IPAddress(v6netmask).netmask_bits()
    ipv6 = ipv6[1]
    ipv6 = ipv6[1:-2]
    ipv6net = netaddr.IPNetwork(ipv6 + "/" + str(cidr6))
    ipv6net = ipv6net.cidr
    networkdict['v4'] = ipv4net
    networkdict['v6'] = ipv6net
    return networkdict