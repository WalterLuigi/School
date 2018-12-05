#!/bin/bash

# This file just splits the full-take.pcap file into two seperate files based on differing ports for
# the related services.


tcpdump -vnn -r full-take.pcap -w weather.pcap port 5556 \
&& tcpdump -vnn -r full-take.pcap -w task.pcap port 7008