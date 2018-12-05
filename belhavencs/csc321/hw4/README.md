## What this does

The bash script takes the second column from the domains.tsv file and does a DNS lookup on the supplied domain names. It outputs the results as lookupdata.txt
The python script takes the data from lookupdata.txt and performs reverse DNS lookups on all the addresses supplied by the bash script. It then maps them back to the original domain names.

## What it outputs

DNSLookup outputs a txt file filled with the addresses garnered by doing a DNS lookup using the dig tool.
ReverseLookup outputs a gv file, ensure you have graphviz installed and added to your path or else this will not work.

## How to replicate
Ensure you do a pip install graphviz, you also must install the binaries and add them to your path. Once you have done this:

1. Run the shell script from the same directory as domains.tsv
2. Next, run the python script once the previous is completed.
3. View output file
4. ?
5. Profit