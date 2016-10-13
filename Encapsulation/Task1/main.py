from  Encapsulation.Task1.Book import Book


def main():

    list_of_books = [Book("Mark Tven", "Tom Soyer", 1900,"Advangere"), Book("Mark Tven", "Tom Soyer", 1900,"Advangere"),
    Book("Alexandr Pyshkin", "Ruslan and Luydmila", 1820, "poem")]

    if list_of_books[0] == list_of_books[1]:
        print("equils books")

    if list_of_books[0] != list_of_books[-1]:
        print("books not equil")

    for item in list_of_books:
        print(item)

main()
