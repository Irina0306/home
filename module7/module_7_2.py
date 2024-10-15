from pprint import pprint
import io
from typing import List, Tuple, TextIO, Any


def custom_write(file_name, strings):

    strings_position = {}
    file = open(file_name, 'w', encoding='UTF-8')

    for i, string in enumerate(strings):
        strings_position[(i + 1, file.tell())] = string
        file.write(f'{string}\n')
    return strings_position
    file.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.'
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

