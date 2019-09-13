# LISTS OPERATIONS
# Merge lists
mylist_1 = ['alpha', 'beta', 'gamma']
mylist_2 = ['tetra', 'zeta']
grouplist = []

grouplist += mylist_1 + mylist_2
print(grouplist)


# difference between 'append' and 'extend', look at bracers in output.

mylist_3 = ['one', 'two', 'three']
mylist_4 = ['four', 'five']

append_result = []
extend_result = []

append_result.append(mylist_3 + mylist_4)
extend_result.extend(mylist_4 + mylist_3)

print(str(append_result) + ' appended list contain '+ str(len(append_result)) + ' elements, because its append')
print(str(extend_result) + ' extended list contain '+ str(len(extend_result)) + ' elements, because its extend')

#DATA STRUCTURE

bogo_list = ['one', 'two', 'three']
bogo_tuple = 'one', 'two', 'three' # you can create a tuple without round bracers, check it print(type(bogo_tuple))
bogo_dict = {'one': 1, 'two': 2, 'three': 3}


exlist = 'stop shooting me'
print(exlist.split())

hello = 'hello hello'
print(hello.count(''))
