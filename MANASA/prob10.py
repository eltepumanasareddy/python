x = lambda a: a + 70
print(x(10))

#1
x = lambda a, b : a * b
print(x(2, 6))


#2
x = lambda a, b, c: a + b + c
print(x(8, 12, 16))

#3
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(8)

print(mydoubler(9))


#4
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(6)

print(mytripler(10))









