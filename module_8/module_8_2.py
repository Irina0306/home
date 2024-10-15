def personal_sum(numbers):
    numbers= []
    result = 0
    incorrect_data = 0
    for i in numbers:
        #if numbers.isnumeric()== True:
            try:
                result += i
                #print(result)
                return result

            except TypeError as exc:

                incorrect_data += 1
                return incorrect_data
        return (result, incorrect_data)

def calculate_average(*numbers):

    for i in numbers:
        try:
            if i == int:

                 return personal_sum(i)/len(personal_sum(i))

        except ZeroDivisionError:
            return 0
        except TypeError:
            print('В numbers записан некорректный тип данных')

print(f'Результат1:{calculate_average('1,2,3')}')
print(f'Результат2:{calculate_average([1,'строка', 3, "еще строка"])}')
print(f'Результат3:{calculate_average(567)}')
print(f'Результат4:{calculate_average([42, 15, 36, 13])}')