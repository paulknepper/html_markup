# rules.py
# matching rules for identifying different types of text for html markup
# designed for python 3.x
import re

class Rules:
    def find_pattern(self, text):
        if self.pattern.match(text): return True
    
class Title(Rules):
    pattern = re.compile(r'^(\b\w+\b[ \t\f\v]{0,2}){1,5}$')

class List(Rules):
    pattern = re.compile(r'^(\d{1,2}\.?)|(\- ?)[ \t\f\v]{0,2}.*?$')


