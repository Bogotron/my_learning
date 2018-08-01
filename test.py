import os
import subprocess
'''
for p_range in range (1, 10):
    ip_range = '172.16.48' + str(p_range)
    result = subprocess.Popen(['ping', '-c', '3', ip_range])
    if result == 0:
        print ("success ping " + p_range)
    elif result == 2:
        print("no responce from " + p_range)
    else:
        print("failed" + str(p_range))


def has_33(numlist):
    return_list = []
    for i in range(len(numlist)):
        if numlist[i] == 3:
            return_list.append(numlist[i])
    print(return_list)


print(has_33([0, 3, 3, 4, 5 , 3]))

'''

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69(2, 8, 6, 8, 9, 3))