
class Avto:

    def __init__(self, mark, model, price):
        self._mark = mark
        self._model = model
        self._price = price

    def __eq__(self, other):
            return self._mark == other.mark and self._model == other.model and self._price == other.price

    @property
    def mark(self):
        return self._mark

    @property
    def model(self):
        return self._model

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self.price = value
        else:
            print("incorrect value")

    def __repr__(self):
        return "Avto({!r} {!r} {!r})".format(self._mark, self._model, self._price)

    def __str__(self):
        return "Car: mark: {}, model: {}, price: {}".format(self._mark, self._model, self._price)


