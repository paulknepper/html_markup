# textparse.py--create html elements from text input

class Parser:
    def __init__(self, element):
        self.element = element

    def markup(self, action, text): # args expected to be text
        method = getattr(self, action+'_element', None)
        if callable(method):
            # 'self' already embedded in method via getattr()
            return method(text) 

    def tag_element(self, text):
        return self.start_tag(text) + self.end_tag(text)
    
    def start_tag(self, text):
        if self.element == 'title': return '<h1>'+text
        if self.element == 'paragraph': return '<p>'+text
        if self.element == 'list': return '<li>'+text

    def end_tag(self, text):
        if self.element == 'title': return '</h1>'
        if self.element == 'paragraph': return '</p>'
        if self.element == 'list': return '</li>'
