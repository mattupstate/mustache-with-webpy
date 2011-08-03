from views.base import View

def map_links(item):
    item['link'] = '/examples/%s' % item['id']
    return item

class ExamplesIndex(View):
    def examples(self):
        return map(map_links, self.data['examples'])
    
class ExamplesShow(View):
    def example(self):
        return self.data['example']
    