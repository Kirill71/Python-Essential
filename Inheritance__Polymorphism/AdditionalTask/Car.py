class Car:

    def __init__(self, mark, model):
        self._mark = mark
        self._model = model

    @property
    def mark(self):
        return self._mark

    @property
    def model(self):
        return self._model

    def __repr__(self):
        return "Car({!r}, {!r})".format(self._mark, self._model)

    def __str__(self):
        return "Car: mark - {}, model - {}".format(self._mark, self._model)

    def __eq__(self, other):
        return self._mark == other.mark and self._model == other.model
