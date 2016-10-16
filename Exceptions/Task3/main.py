from Exceptions.Task3.Employe import Employee

def main():
    list =[Employee("Vasya", "Vasil'ev", "xz", 2013), Employee("Petya", "Petrov", "xz", 2014)]

    for var in list:
        if (var.begin_work_year > 2012):
            print(var)
if __name__ == '__main__':
    main()