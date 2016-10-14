from Inheritance__Polymorphism.Task1 import Editor, ProEditor


def main():
    key = input('Enter license key: ')
    if key == 'kirill21':
        print('Product activated.')
        editor = ProEditor.ProEditor()
    else:
        print('Incorrect license key, reverting to the free version.')
        editor = Editor.Editor()

    editor.view_document()
    editor.edit_document()

if __name__ == '__main__':
    main()