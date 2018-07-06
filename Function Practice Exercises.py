# WARMUP SECTION:

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    elif a % 2 != 0 and b % 2 != 0:
        return a, b
    elif a % 2 != 0:
        return a
    elif b % 2 != 0:
        return b

print(lesser_of_two_evens(8, 5))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    words = []
    for word in text.split():
       words.append(word)
    if words[0][0] == words [1][0]:
        return True
    else:
        return False
print(animal_crackers('Hell Hipopotham'))

# Better decision for ANIMAL CRACKERS
def animal_crackers_2(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False

def makes_twenty(*args):
    if sum(args) == 20 or any(args) == 20:
        return True
    else:
        return False

print(makes_twenty(3, 7, 10))

def makes_twenty_1(*args):
    if sum(args) == 20 or 20 in args:
        return True
    else:
        return False

print(makes_twenty_1(3, 10, 15))

# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'


print(old_macdonald('macdonald'))

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(phrase):
    phrase_list = list(phrase.split())
    return ' '.join(phrase_list[::-1])

print(master_yoda('I am home'))

def master_yoda_1(text):
    return ' '.join(text.split()[::-1])

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(x):
    return 90 <= x <= 110 or 190 <= x <= 210

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

def almost_there_1(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

print(abs(100-90))

print('\n')

# LEVEL 2 PROBLEMS
# FIND 33:Given a list of ints, return True if the array contains a 3 next to a 3 somewhere

def has_33(numlist):
    return_list = []
    for val in numlist:
        if val == 3:
            return_list.append(val)
    if return_list[0] == 3 and return_list[0] == 3:
        return True
    else:return False

print(has_33([3, 0, 0, 3]))

#def has_33(nums):
    #for i in range(0, len(nums) - 1):

        # nicer looking alternative in commented code
        # if nums[i] == 3 and nums[i+1] == 3:

        #if nums[i:i + 2] == [3, 3]:
            #return True

    #return False


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    paper_retutn = ''
    for letter in text:
        paper_retutn += letter * 3
    return paper_retutn

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

'''
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their 
sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment)
exceeds 21, return 'BUST'¶
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
'''

def blackjack(a,b,c):
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
        return sum((a, b, c)) - 10
    else:
        return 'BUST'

print(blackjack(7, 7, 7))

'''
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
'''

:
def summer_69(arr):
