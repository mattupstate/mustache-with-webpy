import views.main as view

class MainIndex(object):
    
    def GET(self):
        v = view.MainIndex()
        v.set('welcome', 'Welcome!')
        return v.render()