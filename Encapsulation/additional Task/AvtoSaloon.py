from Encapsulation import Avto


class AvtoSaloon:

    def __init__(self):
        self.__car_for_sales_list = []

    def add_car(self, car):
        if isinstance(car, Avto.Avto):
            self.__car_for_sales_list.append(car)

    def sale_car(self, car):
        if car in self.__car_for_sales_list and  isinstance(car, Avto.Avto):
            self.__car_for_sales_list.remove(car)

    def __repr__(self):
        return "{}".format(self.__car_for_sales_list)

    def __str__(self):
        string = ""
        for item in self.__car_for_sales_list:
            string += str(item) + " | "
        return string

