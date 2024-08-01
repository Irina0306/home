
class Animal:
    alive =True
    fed =  False
    def __init__(self,name):
        self.name=name
    def eat(self, food, adible=None, edible=None):
        self.food=food
        if self.food== adible:
            fed= True
            print(f'{self.name} съел {food.name}')

        if self.food!= edible:
            print(f'{self.name} не стал есть {food.name}')

class Mammal(Animal):
    fed=True
class Predator(Animal):
    alive=False

class Plant:
    adible =False
    def __init__(self,name):
        self.name=name

class Flower(Plant):
    pass
class Fruit(Plant):
    adible= True


a1= Predator('Волк с Уолл-Стрит')
a2= Mammal('Хатико')
p1=Flower('Цветик-семицветик')
p2=Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)