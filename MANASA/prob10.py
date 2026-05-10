x = lambda a: a + 100
print(x(10))

#1
x = lambda a, b : a * b
print(x(2, 9))


#2
x = lambda a, b, c: a + b + c
print(x(8, 10, 16))

#3
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


#4
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))








