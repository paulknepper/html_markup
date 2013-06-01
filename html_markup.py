# html_markup.py--converts text files to marked up html
# this script is designed for python 3.x
# This version is a true script meant to be called at command line
import sys
from textblock import get_block
from rules import Title, List
from textparse import Parser

"""
This is a basic html markup script.  It takes a text file and applies basic
rules to mark the text up as html, returning an html file.  To use this script,
activate it at the command line like so:
    $ python html_markup.py < inputfile.txt > outputfile.html

This will denote the proper files as stdin or stdout.
"""

print("<!doctype html>")
print("<html><title></title><body>")

infile = sys.stdin
for block in get_block(infile):
    if Title().find_pattern(block):
        print(Parser('title').markup('tag', block))
    elif List().find_pattern(block):
        print(Parser('list').markup('tag', block))
    else:
        # default is always <p> tag
        print(Parser('paragraph').markup('tag', block))
print("</body></html>") # closing tags
