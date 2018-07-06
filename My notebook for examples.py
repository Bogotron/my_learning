# STRINGS
# Operations with strings and strings formating

name = 'Kirill'
age = 29
city = 'Moscow'

print(f'Hello my name is {name}, my age is {age}, i live in {city}')

a = 1
b = 'two'
c = 12.3
print('First Object: {aa}, Second Object: {bb}, Third Object: {cc}'.format(aa=a, bb=b, cc=c))


list_one = ['a', 'g', 't', 'q', 'b']
list_two = ['1', '9', '2', '6', '3']

list_one.sort()
list_three = list_one

list_two.sort()
list_four = list_two

print(list_three)
print(list_four)

# DICTIONARIES

my_dict = {'submarine_1': 'Arkhangelsk', 'submarine_2': 'Novodvinsk', 'codenames': ['nerpa', 'kambala', 'treska'], 'missles': 24}

# несколько примеров работы со словарями
# ключ
print(my_dict['submarine_1'])
# ключ с индексом строки внутри
print(my_dict['codenames'][1])
# работа с int внутри словаря
print(my_dict['missles'] - 12)
# добавляем новый ключ в dict
my_dict['torpedo'] = 4
print(my_dict.items())

# Соединяем два словаря
x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}
z = {**x, **y}

print("It's dict welding ", z)  # {'c': 4, 'a': 1, 'b': 3}

# TUPLES

tup = (0, 1, 1, 1, 2, "one", "two")
print(tup[5])
print(tup.count(1))
print(tup.index('one'))


# SETS
myset = set()
myset.add(1)
myset.add(2)
print(myset)

# Вывод уникальных значений из списка через set
mylist = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, ]
myset_1 = set(mylist)
print(myset_1)

# Ещё пример, не забывать ставить в начале тип SET, иначе будет STRING
myset_2 = set('Mississippi')
print(myset_2)

# BOOLEANS

print(1 > 2)
print(2 == 2)
b = None
print(type(b))

#FILES
#open files


# call the help topic
help(str)