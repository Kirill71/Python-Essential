class Employee:
    def __init__(self, name, surname, deportment, begin_work_year):
        if isinstance(name, str) and isinstance(surname, str) and isinstance(deportment, str) \
                and isinstance(begin_work_year, int):
            self._name = name
            self._surname = surname
            self._deportment = deportment
            self._begin_work_year = begin_work_year
        else:
            raise ValueError()

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def department(self):
        return self._department

    @property
    def begin_work_year(self):
        return self._begin_work_year

    def __str__(self):
        return """Employe:\n
        name: {}, surname: {},  department: {}, begin_work_year: {}""".format(self._name, self._surname, self._deportment, self._begin_work_year) + "."
