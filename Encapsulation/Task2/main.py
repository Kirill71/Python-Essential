from  Encapsulation.Task2.improvedBook import ImprovedBook


def main():

    list_of_books = [ImprovedBook("Mark Tven", "Tom Soyer", 1900, "Advangere", "Good book"),
                     ImprovedBook("Mark Tven", "Tom Soyer", 1900, "Advangere", "Good book"),
    ImprovedBook("Alexandr Pyshkin", "Ruslan and Luydmila", 1820, "poem", "Intresting book")]

    if list_of_books[0] == list_of_books[1]:
        print("equils books")

    if list_of_books[0] != list_of_books[-1]:
        print("books not equil")

    for item in list_of_books:
        print(item)

main()
