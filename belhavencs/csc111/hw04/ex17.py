#!/usr/bin/python3
#Imports modules pathlib and os
import os; from pathlib import Path;
#Defines from_file and to_file as userinput names in the current working directory
from_file = Path.cwd() /input("Input> "); 
to_file = Path.cwd() / input("Output> ");
#Opens and defines in_file as from_file, reads it and passes the data to indata, defines outfile as a writable version of to_file
#then writes the data from the in_file to the out_file

with open(from_file, 'r') as in_file: indata = in_file.read(); out_file = open(to_file, 'w'); out_file.write(indata)
