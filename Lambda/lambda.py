x = lambda a,b,c: a + b + c
print(x(2,5,4))

def myfunc(n):
    return lambda a: a * n

mytripler = myfunc(3)
mydoubler = myfunc(2)
print(mytripler(11))
print(mydoubler(10))

