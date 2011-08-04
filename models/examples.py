class Example(object):
    '''This is a fake/mock model object with two super simple static methods'''
    
    @staticmethod
    def all():
        '''Get a list of Example objects'''
        result = []
        for i in range(1,10):
            result.append({ 'id': i, 'name': 'Example %s' % i })
        return result;
    
    @staticmethod
    def get_example(id):
        '''Get an Example object by ID'''
        for e in Example.all():
            if e['id'] is id:
                return e
        return None
  
