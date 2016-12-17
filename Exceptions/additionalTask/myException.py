class MyException(Exception):

    def __init__(self, value):
        super().__init__(value)
        print(value)


def raise_exception():
        raise MyException("bla-bla-bla")


def main():
    try:
        raise_exception()
    except MyException as e:
        print("catch")

if __name__ == '__main__':
    main()