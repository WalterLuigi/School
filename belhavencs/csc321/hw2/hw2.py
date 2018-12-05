#!/usr/bin/python

import ipaddress, netifaces, netaddr




def sanitize_ip(ip):
    if '%' in ip:
        return ip.split('%')
    if '/' in ip:
        return ip.split('/')




def get_interfaces():
    """Return a list of all the interfaces on this host

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (list) List of interfaces for this host




    Local: ['lo', 'eno1', 'wlp2s0', 'br-45489b396538', 'br-585a983c21ed', 
            'br-9278f667c775', 'br-b2d3ac665dd3', 'br-bc0ee0bf4728', 'docker0', 
            'vethbbba13f', 'vethaf99571', 'vethc850f8a', 'veth040905e']
    """

    return netifaces.interfaces()



def get_mac(interface: str):
    """For the given interface string, return the MAC address as a
    string

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (str) MAC address



    Local: 'a0:a8:cd:82:83:d'
    """

    addrs = netifaces.ifaddresses(interface)
    mac = addrs[netifaces.AF_LINK]
    mac = mac[0]
    mac = mac['addr']
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



    Home: {'v4': IPv4Address('10.0.0.10'),
           'v6': IPv6Address('2601:3c7:8201:3aa0:600b:d309:ac54:897e')

    Belhaven: {'v4': IPv4Address('192.168.181.49')
               'v6': IPv6Address('fe80::8d2e:9b72:42de:a0b0')}
    """

    ipdict = {}
    addrs = netifaces.ifaddresses(interface)
    ipv4 = addrs.get(netifaces.AF_INET, [{}])[0]
    ipv4 = ipv4['addr']
    ipv4 = ipaddress.IPv4Address(ipv4)
    ipv6 = addrs.get(netifaces.AF_INET6, [{}])[0]
    ipv6 = ipv6['addr']
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



    Home: {'v4': IPv4Address('255.255.255.0'),
           'v6': IPv6Address('ffff:ffff:ffff:ffff::')}

    Belhaven: {'v4': IPv4Address('255.255.240.0'),
               'v6': IPv6Address('ffff:ffff:ffff:ffff::')}
    """

    netmaskdict = {}
    addrs = netifaces.ifaddresses(interface)
    ipv4 = addrs.get(netifaces.AF_INET, [{}])[0]
    ipv4 = ipv4['netmask']
    ipv4 = ipaddress.IPv4Address(ipv4)
    ipv6 = addrs.get(netifaces.AF_INET6, [{}])[0]
    ipv6 = ipv6['netmask']
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



    Home: {'v4': IPNetwork('10.0.0.10/32'), 'v6': IPNetwork('2601:3c7:8201:3aa0::/64')}

    Belhaven: {'v4': IPNetwork('192.168.176.0/20'), 'v6': IPNetwork('fe80::/64')}
    """

    networkdict = {}
    addrs = netifaces.ifaddresses(interface)
    ipv4 = addrs.ge([netifaces.AF_INET, [{}])[0]
    v4netmask = ipv4[3]
    v4netmask = v4netmask[1:-2]
    cidr4 = netaddr.IPAddress(v4netmask).netmask_bits()
    ipv4 = ipv4[1]
    ipv4 = ipv4[1:-2]
    ipv4net = netaddr.IPNetwork(ipv4 + "/" + str(cidr4))
    ipv4net = ipv4net.cidr
    ipv6 = addrs.get(netifaces.AF_INET6, [{}])[0]
    v6netmask = ipv6[3]
    v6netmask = v6netmask[1:-6]
    cidr6 = netaddr.IPAddress(v6netmask).netmask_bits()
    ipv6 = ipv6[1]
    ipv6 = ipv6[1:-2]
    ipv6net = netaddr.IPNetwork(ipv6 + "/" + str(cidr6))
    ipv6net = ipv6net.cidr
    networkdict['v4'] = ipv4net
    networkdict['v6'] = ipv6net
    return networkdict