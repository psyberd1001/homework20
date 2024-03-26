class House:

    numberOfFloors = 10

    def function1(self, nuberOfFloors):
        for i in range(nuberOfFloors):
            print('Текущий этаж равен ', i + 1)


house = House()
house.function1(house.numberOfFloors)
