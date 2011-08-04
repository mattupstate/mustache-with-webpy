from controllers.base import Controller

class MainIndex(Controller):
    '''Main Index (Home Page). URL: /'''
    
    def GET(self):
        self.view.set('welcome', 'Welcome!')
        return self.view.render()