from views.base import View

class MainIndex(View):
    def welcome(self):
        return self.data['welcome']
    