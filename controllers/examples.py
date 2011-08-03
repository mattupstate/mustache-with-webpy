import views.examples as views

examples = [
    { 'id': 1, 'name': 'Lorem Ipsum' },
    { 'id': 2, 'name': 'Dolor Sit'},
]

def get_example(id):
    for e in examples:
        if e['id'] is id:
            return e
    return None

class ExamplesIndex(object):
    def GET(self):
        v = views.ExamplesIndex()
        v.set('examples', examples)
        return v.render()
    
class ExamplesShow(object):
    def GET(self, example_id=None):
        v = views.ExamplesShow()
        v.set('example', get_example(int(example_id)))
        return v.render()
        
