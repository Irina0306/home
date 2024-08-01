class Hause:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)

        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print('Такого этажа не существует')

        else:

            for i in range(1, new_floor):
                print(i)
            return self.new_floor



h1 = Hause('Эталон', 25)
h2 = Hause('Самолет', 2)
print(h1.go_to(5))
print(h2.go_to(10))
