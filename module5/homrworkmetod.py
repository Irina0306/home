class Hause:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors += floors
        return self.numberOfFloors



h2 = Hause(10)
print(h2.setNewNumberOfFloors(10))
