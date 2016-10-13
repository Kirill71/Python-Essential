class Book:

    def __init__(self,  author, name, publish_year, genre):
        self._author = author
        self._name = name
        self._publish_year = publish_year
        self._genre = genre

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def publish_year(self):
        return self._publish_year

    @publish_year.setter
    def publish_year(self, value):
        self._publish_year = value

    @property
    def genre(self):
        return self._genre

    def __repr__(self):
        return "Book({!r}, {!r}, {!r}, {!r})".format(self._author, self._name, self._publish_year, self._genre)

    def __str__(self):
        return "Book: {}, {}, {}, {}.".format(self._author, self._name, self._publish_year, self._genre)

    def __eq__(self, other):
        return self._author == other.author \
               and self._name == other.name \
               and self._publish_year == other.publish_year \
               and self._genre == other.genre

    def __ne__(self, other):
        return not self == other
