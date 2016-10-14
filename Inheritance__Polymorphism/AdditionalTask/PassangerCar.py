from Inheritance__Polymorphism.AdditionalTask.Car import Car


class PassengerCar(Car):

    def __init__(self, mark, model, number_of_passengers):
        super().__init__(mark, model)
        self._number_of_passengers = number_of_passengers

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    def __repr__(self):
        return " PassengerCar({!r}, {!r}, {!r})".format(self._mark, self._model, self._number_of_passengers)

    def __str__(self):
        return "Pessanger" + super().__str__() + ", number of passengers - {}".format(self._number_of_passengers)

    def __eq__(self, other):
        return super().__eq__() and self._number_of_passengers == other.number_of_passengers


