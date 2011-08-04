from models.examples import Example

class ExamplesIndex(object):
    '''Examples Index. URL: /examples/'''
    
    def GET(self):
        self.view.set('examples', Example.all())    # 
        return self.view.render()
    
class ExamplesShow(object):
    '''Examples Show. URL: /examples/<example_id>/'''
    
    def GET(self, example_id=None):
        self.view.set('example', Example.get_example(int(example_id)))
        return self.view.render()
        
