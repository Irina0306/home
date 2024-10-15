def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
            try:
                result += i

            except TypeError as exc:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчета-{i}')
                #incorrect_data += 1

    return (result,incorrect_data)

def calculate_average(numbers):
    try:
        print(personal_sum(numbers)[0]/len(numbers)-personal_sum(numbers)[1])

    except ZeroDivisionError as e:
        return 0
    except TypeError as e:
        print('В numbers записан некорректный тип данных')

print(f'Результат1:{calculate_average('1,2,3')}')
print(f'Результат2:{calculate_average([1,'строка', 3, "еще строка"])}')
print(f'Результат3:{calculate_average(567)}')
print(f'Результат4:{calculate_average([42, 15, 36, 13])}')
#print(personal_sum([42,15,36,13]))