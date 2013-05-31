# html_markup.py--converts text files to marked up html
# this script is designed for python 3.x
# This version is a true script meant to be called at command line
import sys
from textblock import get_block

print("<!doctype html>")
print("<html><title></title><body>")

infile = sys.stdin
for block in get_block(infile):
    if Title().find_pattern(block):
        pass
print("</body></html>") # closing tags
