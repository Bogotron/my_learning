# Functions and Methods Homework
import string
import math

def vol(rad):
    return round((4/3 * math.pi * (rad**3)), 3)

print(vol(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    if num in range(low, high+1):
        print(f'The num {num} is in range {low} and {high}')
    else:
        print(f'The num {num} is not in range {low} and {high}')

ran_check(7, 1, 10)
ran_check(12, 1, 10)

def ran_bool(num,low,high):
    return num in range(low, high+1)

print(ran_bool(7, 1, 10))
print(ran_bool(17, 1, 10))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(s):
    lower = 0
    upper = 0

    for letter in s:
        if letter in string.ascii_lowercase:
            lower += 1
        elif letter in string.ascii_uppercase:
            upper += 1
        else:
            continue
    print(f'Original String: {s}')
    print(f'No. of Upper case characters : {lower}')
    print(f'No. of Upper case characters : {upper}')


print('\n')
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    return list(set(lst))

print('\n')
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

#Write a Python function to multiply all the numbers in a list.

def multiply(nums):
    mnum = 1
    for num in nums:
        mnum *= num
    return mnum


print('\n')
print(multiply([1,2,3,-4]))


def palindrome(s):
    return s[0:] == s[::-1]

print(palindrome('helleh'))

teststr = 'hello world'
teststr.lower()

def ispangram(str):
    alphabet = string.ascii_lowercase
    alphabet_count = 0
    for letter in alphabet:
        if letter in str.lower():
            alphabet_count += 1
    if alphabet_count == len(alphabet):
        return True
    else:
        return False
    pass

print('\nPan:')
print(ispangram('What are you looking for?'))
print(ispangram("The quick brown fox jumps over the lazy dog"))


def ispangram_1(str):
    alphabet = string.ascii_lowercase
    return set(str.lower()) >= set(alphabet)

print('\nPan 1:')
print(ispangram_1('What are you looking for?'))
print(ispangram_1("The quick brown fox jumps over the lazy dog"))