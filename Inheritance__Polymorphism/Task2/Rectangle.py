from Inheritance__Polymorphism.Task2.GraphicalObject import GraphicalObject


class Rectangle(GraphicalObject):
    def __init__(self, width, height, text=""):
        super().__init__()
        self._width = width
        self._height = height
        self._text = text

    def draw(self):
        if self._text:
            padded_text = ' ' + self._text + ' '
        else:
            padded_text = self._text

        padded_text_len = len(padded_text)
        left_padding = round((self._width - padded_text_len)/2)
        left = '*' * left_padding
        right = '*' * (self._width - left_padding - padded_text_len)
        for i in range(self._height):
            if i == round(self._height/2):
                print(left, padded_text, right, sep='')
            else:
                print('*' * self._width)

