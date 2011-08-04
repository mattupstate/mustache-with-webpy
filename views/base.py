import pystache
import re

class View(pystache.View):
    '''Base view object. This should always be inherited by your more specific view
    classes. Its here that you could add common data that all templates might be
    interested in such as session data, flash variables, site configuration data, etc.'''
    
    template_path = 'templates'
    template_name = 'default'
    model = {
        'base_url': '/', # Could come from web.py context? 
        'page_title': '&#123&#123mustache&#125&#125 with web.py', # Could come from a configuration value?
        'section_class': 'none', # section class name
        'page_class': 'none-none' # page class name
    }
       
    def _generate_template_path(self):
        '''Generates the path to the template body based on the class name. This relies 
        on following a convention. For example, the view class ExamplesShow maps to the
        template "/templates/examples/show.mustache"'''
        return re.sub('((?=[A-Z][a-z])|(?<=[a-z])(?=[A-Z]))', '/', self.__class__.__name__).lower()[1:]
    
    def set(self, key, value):
        '''Adds a value to the view's model'''
        self.model[key] = value
        return self
    
    def base_url(self):
        '''The website's base URL'''
        return self.model['base_url']
    
    def page_title(self):
        '''The page title'''
        return self.model['page_title']
    
    def section_class(self):
        '''The section class name. Example: projects'''
        return self.model['section_class']
    
    def page_class(self):
        '''The page class name. projects-index'''
        return self.model['page_class']
    
    def body(self):
        '''The template to include as the body'''
        return '{{>%s}}' % self._generate_template_path() 