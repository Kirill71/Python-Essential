from Encapsulation.Task2.Book import Book


class ImprovedBook:

    def __init__(self,  author, name, publish_year, genre, recall):
        self._book = Book(author, name, publish_year, genre)
        self._recall = recall

    @property
    def book(self):
        return self._book

    @property
    def recall(self):
        return self._recall

    @recall.setter
    def recall(self, value):
        self._recall = value

    def __repr__(self):
        return "Book({!r}{!r})".format(self._book, self._recall)

    def __str__(self):
        return "Book: {} {}.".format(self._book, self._recall)

    def __eq__(self, other):
        return self._book == other.book and self._recall == other.recall

    def __ne__(self, other):
        return not self == other
