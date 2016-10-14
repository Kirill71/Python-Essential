class GraphicalObject(object):
    pass


class Rectangle(GraphicalObject):
    pass


class Clickable(object):
    pass


class Button(Rectangle, Clickable):
    pass


def main():
    for cls in [GraphicalObject, Rectangle, Clickable, Button]:
        print(cls.mro())

if __name__ == '__main__':
    main()
