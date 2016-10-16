
class Calculator:
    __res = 0.0

    @staticmethod
    def calculate(a, b, op):
        """

        :param a: operator 1 (integer or real number),
        :param b: operator 2 (integer or real number),
        :param op: operation sign. Supported:(+, -, *, /, ^)
        :return: nothing
        """
        operation_list = ["+", "-", "*", "/", "^"]
        try:
            if op not in operation_list:
                raise ValueError("Unsupported operation")
            if op == operation_list[0]:
                __res = Calculator.__add(a, b)
            elif op == operation_list[1]:
                __res = Calculator.__sub(a, b)
            elif op == operation_list[2]:
                __res = Calculator.__mul(a, b)
            elif op == operation_list[3]:
                __res = Calculator.__div(a, b)
            elif op == operation_list[4]:
                __res = Calculator.__pow(a, b)
        except (ValueError, ZeroDivisionError, ArithmeticError) as ex:
            print(ex)
        else:
            print(__res)

    @staticmethod
    def __add(a, b):
        return a + b

    @staticmethod
    def __mul(a, b):
        return a * b

    @staticmethod
    def __sub(a, b):
        return a - b

    @staticmethod
    def __div (a, b):
        if b == 0.0:
            raise ZeroDivisionError("Divizion by zero")
        else:
            return a/b

    @staticmethod
    def __pow(a, b):
        if a == 0.0 and b < 0:
            raise ArithmeticError("Zero in negative power")
        return a ** b
