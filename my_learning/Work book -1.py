# В этом файле я храню полезные заметки по програмированию на питоне.

# Two ways to check letters in word.

st = 'Sam Sampson Print only the words that start with s in this sentence'

for word in st.split():
    if word[0].lower() == 's':  # более предпочтительный вариант
        print(word)

print('\n')

for word in st.split():
    if word[0] == 's' or word[0] == 'S':
        print(word)


# enumerate
# Notice the tuple unpacking!

for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))

# Functions
# Skyline function

def myfunc(x):
    out = []
    for i in range(len(x)):
        if i % 2 == 0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

print(myfunc('where are you my little pony'))



my_str = ''
print(my_str.join('sdtsgsdgsd'))