import pystache
import re

class View(pystache.View):
    
    def __init__(self, template=None, context=None, **kwargs):
        super(View, self).__init__(template, context)
        self.template_path = 'templates'
        self.template_name = 'default'
        self.data = {
            'base_url': '/',
            'page_title': '&#123&#123mustache&#125&#125 with web.py',
            'section_class': 'none',
            'page_class': 'none-none'
        }
        
    def _generate_template_path(self):
        return re.sub('((?=[A-Z][a-z])|(?<=[a-z])(?=[A-Z]))', '/', self.__class__.__name__).lower()[1:]
    
    def set(self, key, value):
        self.data[key] = value
        return self
    
    def base_url(self):
        return self.data['base_url']
    
    def page_title(self):
        return self.data['page_title']
    
    def section_class(self):
        return self.data['section_class']
    
    def page_class(self):
        return self.data['page_class']
    
    def body(self):
        return '{{>%s}}' % self._generate_template_path() 