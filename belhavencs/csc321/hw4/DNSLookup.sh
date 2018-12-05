#!/bin/bash

sed 1d ./domains.tsv | while read line
do
	domain=$(awk -F"\t" '{print $2}' <<< "$line")
	domaindata=$(dig +short $domain)
	linedata=$(printf "$domain $domaindata")
	echo $linedata >> lookupdata.txt
done