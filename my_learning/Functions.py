def myfunc(name):
    print(f'My name is {name}') # f-formating

myfunc('John')



def myfunc1(a, b, c):
    if c == True:
        return a
    else:
        return b

print(myfunc1('hello', 'bye', False))

def multiple (x, y):
    return x * y

print(multiple(10, 5))

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
print(is_even(6))

def is_less(x, y):
    '''
    Compare two argumets
    :param x: Integer
    :param y: Integer
    :return:  Boolean
    '''
    return x < y

print(is_less(10, 20))
help(is_less)

help(sum)