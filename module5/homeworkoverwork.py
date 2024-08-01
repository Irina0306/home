class Building:
    def __init__(self, numberOfFloors,buildingType):
        self.numberOfFloors= numberOfFloors
        self.buildingType= buildingType
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


h1 = Building( 2, 'кирпичный')
h2 = Building( 2, 'деревянный')
h2.buildingType= 'кирпичный'
print(h1==h2)