from Inheritance__Polymorphism.Task2.Button import Button
from Inheritance__Polymorphism.Task2.Rectangle import Rectangle

def main():
    rect = Rectangle(20, 5)
    rect.draw()
    rect.click()

    print()

    button = Button()
    print(Button.mro())
    button.draw()
    button.click()

if __name__ == '__main__':
    main()