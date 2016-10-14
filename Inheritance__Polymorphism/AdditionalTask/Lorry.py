from Inheritance__Polymorphism.AdditionalTask.Car import Car


class Lorry(Car):

    def __init__(self, mark, model, capacity):
        super().__init__(mark, model)
        self._capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    def __repr__(self):
        return " Lorry({!r}, {!r}, {!r})".format(self._mark, self._model, self._capacity)

    def __str__(self):
        return "Lorry" + super().__str__() + ", capacity - {}".format(self._capacity)

    def __eq__(self, other):
        return super().__eq__() and self._capacity == other.capacity
