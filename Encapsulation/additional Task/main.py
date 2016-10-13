from Encapsulation import Avto, AvtoSaloon


def main():
    saloon = AvtoSaloon.AvtoSaloon()
    saloon.add_car(Avto.Avto("BMW", "X5", 1000000))
    saloon.add_car(Avto.Avto("Porshe", "Carrera", 100000))
    saloon.add_car(Avto.Avto("Lada", "Kalina", 10))
    print(saloon)
    saloon.sale_car(Avto.Avto("Lada", "Kalina", 10))
    print(saloon)


main()
