from views.base import View

class MainIndex(View):
    '''Main Index (Home Page) view class. URL: /'''
    
    def welcome(self):
        '''Welcome message'''
        return self.model['welcome']
    