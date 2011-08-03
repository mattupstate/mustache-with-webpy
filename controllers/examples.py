import views.examples as views
from models.examples import Example

class ExamplesIndex(object):
    def GET(self):
        v = views.ExamplesIndex()
        v.set('examples', Example.all())
        return v.render()
    
class ExamplesShow(object):
    def GET(self, example_id=None):
        v = views.ExamplesShow()
        v.set('example', Example.get_example(int(example_id)))
        return v.render()
        
