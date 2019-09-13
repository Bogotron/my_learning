# Syntax of a while loop
# while some_boolean_condition:
#   do something

x = 0

while x < 10:
    print(x)
    x += 1
else:
    print('x is bigger or equally 10')

# Break, continue, pass


y = 0

while y < 10:
    print(f'y is still smaller then 10: {y}')
    y += 1
    if y == 5:
        print(f'BINGO!!! y is {y}')
    else:
        print('continuing')

#Break

while True:
    stuff = input("String to capitalize [type q to quit}")
    if stuff == "q":
        break
    print(stuff.upper())




