from views.base import View

def map_links(item):
    '''Adds a generated link property to an Example object'''
    item['link'] = '/examples/%s' % item['id']
    return item

class ExamplesIndex(View):
    '''Examples Index view class. URL: /examples/'''
    
    def examples(self):
        '''A list of examples with generated links'''
        return map(map_links, self.model['examples'])
    
class ExamplesShow(View):
    '''Examples Show view class. URL: /examples/<example_id>/'''
    
    def example(self):
        '''A specific Example object'''
        return self.model['example']
    