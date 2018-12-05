#!/usr/bin/python
# Imports sys
import sys
# Defines script, input_encoding, and error from sys.argv
script, input_encoding, error = sys.argv

# Defines function main and passes it three values
def main(language_file, encoding, errors):
    line = language_file.readline()

# Starts an if statement for line
    if line:
    # Calls print_line function and passes line, encoding, and errors
        print_line(line, encoding, errors)
    # Calls main with language_file, encoding, and errors and returns the value to main
        return main(language_file, encoding, errors)

# Defines function print_line
def print_line(line, encoding, errors):
    # Defines next_lang as line.strip
    next_lang = line.strip()
    # Defines raw_bytes as next_lang.encode
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # Defines $cooked_string as $raw_bites.decode
    cooked_string = raw_bytes.decode(encoding, errors=errors)
	# Prints $raw_bytes <===> $cooked_stringopen
    print(raw_bytes, "<===>", cooked_string)
   
# Opens languages.txt with utf-8 encoding and passes it to $languages
languages = open("languages2.txt", encoding="utf-8")
# Calls function main and passes the value of languages, input_encoding, and error
main(languages, input_encoding, error)
