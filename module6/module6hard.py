class Figure:
    def __init__(self,filled, sides, color,sides_count=0):
        self.sides_count= sides_count
        self.__sides= sides
        self.__color=color
        self.filled= filled
    def get_color(self):

        return self.__color

    def __is_valid_color(self,r,g,b):
        self.r=r
        self.g = g
        self.b =b
        if 0<= r <= 255 and 0<= g <= 255
            for g in range(0,255):
                for b in range (0,255):
                   return  True
        else :
            return False

    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color=r,g,b


    def __is_valid_sides(self,*args,a):
        self.args=args


    def get_sides(self):
        return self.__sides

    def __len__(self, perimeter=0):
        self.perimeter= perimeter
        return self.perimeter


    def set_sides(self,*new_sides):
        self.new_sides= new_sides
        if len(self.new_sides)== self.sides_count:




class Circle(Figure):
    def __init__(self,sides_count=1,sides,color, filled, radius):
        super().__init__(sides, color, filled)
        self.__radius = __radius
        self.__radius= __sides/2*3.14


    def get_square(self, square):
        self.square= square
        self.square = 3,14* self.__radius**2
        return self.square

class Triangle(Figure):
    def __init__(self,sides_count=3,sides, color, filled, height):
        super().__init__(sides, color, filled)
        self.__height =__height
    def get_square(self):



class Cube(Figure):
    def __init__(self,sides_count=12,__sides,__color, filled,a):
        super().__init__(__sides,__color, filled)
        self.a =a
        __sides= (a,a,a,a,a,a,a,a,a,a,a,a)
    def get_volume(self,v):
        self.v =v
        v= self.a**3
        return v

circle1= Circle((200,200,100),10)#(Цвет стороны)
cube1= Cube((222,35,130),6)
circle1.set_color(55,66,77)
print(circle1.get_color())
cube1.set_color(300,70,15)#Не изменится
print(cube1.get_color())
cube1.set_sides(5,3,12,4,5)#Не изменится
print(cube1.get_sides())
circle1.set_sides(15)# Не изменится
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())








