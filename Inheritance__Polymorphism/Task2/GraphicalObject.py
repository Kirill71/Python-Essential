
class GraphicalObject(object):

    def click(self):
        try:
            self.on_click()
        except AttributeError:
            print(self.__class__.__name__, 'is not clickable')
