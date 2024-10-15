my_dict={'Vasia':1975,'Egor':1999,'Masha':2002}
print(my_dict)
print(my_dict['Egor'])
print(my_dict.get('Max'))
my_dict.update({'Misha':1995,'Lena':1996})
del my_dict['Masha']
a=my_dict.pop('Egor')
print(a)
print(my_dict)

my_set={'apple', 10,True,'a'}
print(my_set)
my_set.add((1,2,3))
my_set.remove(10)
print(my_set)


