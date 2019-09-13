my_num = 123
my_str = 'this is string'
my_list = ['one', 'two', 'three']
my_tup = ('one', 'two', 'three')
my_dict = {'one': 'un', 'two': 'deux', 'three': 'trois'}

# Numbers basic expressions and logic

a = 4 * (6 + 5)
b = 4 * 6 + 5
c = 4 + 6 * 5
print(a, b, c)

d = 3 + 1.5 + 4
print(d, type(d))

e = 6**2    # Square
f = 6**0.5  # Square root:
print(e, f)

# String basic expressions and logic

g = 'hello'

print(g[1])
print(g[::-1])

print(g[4], g[-1])

# List basic expressions and logic

h = [0] * 3
j = [0, 0, 0]

print(h, j)

k = [1, 2, [3, 4, 'hello']]
p = [5, 3, 4, 6, 1]

k[2][2] = 'goodbye'
p.sort()

print(k, p)

# Dictionary basic expressions and logic
z = {'simple_key': 'hello'}
x = {'k1': {'k2': 'hello'}}
w = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
v = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
vv = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
vv['k1'][2]['k2'][1]['tough'][2][0] = 'salut'

print(z['simple_key'])
print(x['k1']['k2'])
print(w['k1'][0]['nest_key'][1][0])
print(v['k1'][2]['k2'][1]['tough'][2][0])
print(vv['k1'][2]['k2'][1]['tough'][2][0])

# Set basic expressions and logic

dd = [1,2,2,33,4,4,11,22,3,3,2]
print(set(dd))

#Booleans

print(2 > 3)
print(2 <= 3)
print(3 == 2.0)
print(3.0 == 3)
print(4**0.5 != 2)

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1'])