from Inheritance__Polymorphism.Task2 import Clickable,Rectangle


class Button( Rectangle.Rectangle, Clickable.Clickable):
    def __init__(self, width=25, height=5, text=None):
        if text is None:
            text = self.__class__.__name__
        super().__init__(width, height, text)
