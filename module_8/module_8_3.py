class IncorrectVinNumber(Exception):
    def __init__(self, message, *args):
        self.message= message
class IncorrectCarNumber(Exception):
    def __init__(self, message, *args):
        self.message= message


class Car:
    def __init__(self,model,vin, numbers):
        #model= str
        #vin= int
        #numbers = str
        self.model= model
        if (self.__is_valid_vin(vin)):
            self._vin = vin
        if self.__is_valid_numbers(numbers):
            self._numbers = numbers


    def __is_valid_vin(self,vin_number):
        if not isinstance(vin_number,int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        #else:
            #return True
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

            return True

    def __is_valid_numbers(self,numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumber('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumber('Неверная длина номера')





try:
    first= Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second= Car('Model2', 300, 't001tp')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third= Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

