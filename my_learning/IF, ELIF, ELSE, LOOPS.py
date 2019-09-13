mylist = list(range(15)) # New range in python 3, write type of data
print(mylist)

# Append loop
mylist_2 = []
for val in range(11):
    mylist_2.append(val)
print(mylist_2)

#Checking odd numbers

for elem in mylist:
    if elem % 2 == 0:
        print(elem)
    else:
        print(str(elem) + ' is odd number')
        print(f'Odd number: {elem}') # f string literal formatting

# Another example of for loop

list_sum = 0
for elem in mylist:
    list_sum = list_sum + elem
    print(list_sum)

print(list_sum)

list_of_tup = [(1, 2), (3, 4), (5, 6), (7, 8)] # unpacking tuple with indexing
for elem in list_of_tup:
    print(elem[1])


for (a, b) in list_of_tup:   # unpacking tuple
    print(f'this is a: {a}')
    print(f'this is b: {b}')


# iterating in dictionaries

d = {'k1': 1, 'k2': 2, 'k3': 3}

for key in d:
    print(key)

for key, value in d.items():
    print(f'this is key: {key}')
    print(f'this is value: {value}')

for key, value in d.items():
    if key == 'k2' and value == 2:
        print(key, value)

# Внутри словаря содержаться множества обозначенные фигурными скобками, словарь это ключ и значение, а множество
# это всего лишь последовательность значений
drinks = {
    'martini':{'vodka', 'vermouth'},
    'black russian':{'vodka', 'kahlua'},
    'white russian':{'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, ingridients in drinks.items():
    if 'vodka' in ingridients:
        print(f'vodka in: {name}')

for name, ingr in drinks.items():
    if 'vodka' and 'vermouth' in ingr:
        print(f'vodka and vermouth in: {name}')

# Пример с оператором пересечения множеств '&', выводит напитки где содержится vermouth или orange juice
for name1, ingr in drinks.items():
    if ingr & {'vermouth', 'orange juice'}:
        print(f'  vermouth or orange juice in: {name1}')

# Index counting

mystring = "Hello world!"
index_count = 0

for letter in "Hello world!":
    if letter == " ":
        continue
    print("At index {} the letter is {}".format(index_count, letter))
    index_count += 1

print('\n')
print('\n')

# Ennumerate function
for index, letter in enumerate(mystring):
    print(index)
    print(letter)
    print('\n')

for i, l in enumerate(mystring):
    print('At index: {} letter is {}'.format(i,l))

# ZIP function