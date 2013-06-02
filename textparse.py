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
        bold = "<strong>" if text.isupper() else ''
        if self.element == 'first_title': return '<h1>{}'.format(bold)+text
        if self.element == 'title': return '<br><h3>{}'.format(bold)+text
        if self.element == 'paragraph': return '<p>{}'.format(bold)+text
        if self.element == 'list': return '<li>{}'.format(bold)+text

    def end_tag(self, text):
        bold = "</strong>" if text.isupper() else ''
        if self.element == 'first_title': return '{}</h1><br>'.format(bold)
        if self.element == 'title': return '{}</h3>'.format(bold)
        if self.element == 'paragraph': return '{}</p>'.format(bold)
        if self.element == 'list': return '{}</li>'.format(bold)
