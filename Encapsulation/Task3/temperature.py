class Temperature:

    __one_cels = 33.8

    def __init__(self, temperature):
         self._temperature = temperature

    @property
    def temperature_f(self):
        return self._temperature

    @temperature_f.setter
    def temperature_f(self, value):
        self._temperature = value

    @property
    def temperature_c(self):
            return self._temperature * self.__one_cels

    @temperature_c.setter
    def temperature_c(self, value):
        self._temperature = (value * self.__one_cels)

    def __repr__(self):
        return "Temperature({}F, {}C)".format(self.temperature_f, self.temperature_c)

    def __str__(self):
        return "Temperature: {}F, {}C".format(self.temperature_f, self.temperature_c)