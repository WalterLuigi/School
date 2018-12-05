#!/usr/bin/env python 
import netifaces


def get_interfaces():
    """Return a list of all the interfaces on this host

    Args:
      interface (str): String representation of the interface
          (e.g. "eth0" or "en0")

    Returns: (list) List of interfaces for this host
    """

    return netifaces.interfaces()

def main():
    print(get_interfaces())

if __name__ == '__main__':
    main()