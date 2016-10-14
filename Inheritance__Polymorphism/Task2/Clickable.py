

class Clickable(object):
    def on_click(self):
        print(self.__class__.__name__, 'clicked')


