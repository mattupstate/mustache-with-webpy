class Example(object):
    @staticmethod
    def all():
        return [
            { 'id': 1, 'name': 'Lorem Ipsum' },
            { 'id': 2, 'name': 'Dolor Sit'},
        ]
    
    @staticmethod
    def get_example(id):
        for e in Example.all():
            if e['id'] is id:
                return e
        return None
  
