# rules.py
# matching rules for identifying different types of text for html markup
# designed for python 3.x
import re

class Rules:
    def find_pattern(self, text):
        if self.pattern.match(text): return True
    
class Title(Rules):
    pattern = re.compile(r'^(\w ?){1,5}$')


