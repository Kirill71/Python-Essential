from Inheritance__Polymorphism.AdditionalTask import Car,PassangerCar,Lorry


def main():
    car_list = [Car.Car("Lada", "Calina"),
                PassangerCar.PassengerCar("Porshe", "Carrera", 5),
                Lorry.Lorry("VAZ", "Ural", 100)]

    for car in car_list:
        print(car)

if __name__ == '__main__':
    main()
