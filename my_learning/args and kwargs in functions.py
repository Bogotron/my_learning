def myfunc(*args):
    out = []
    for num in args:
        if num%2==0:
            out.append(num)
    return out

print(myfunc(10, 12, 13, 15, 20))