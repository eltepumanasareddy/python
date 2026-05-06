x = lambda a: a + 8
print(x(6))

#1
x = lambda a, b : a * b
print(x(4, 5))

#2
x = lambda a, b, c: a + b + c
print(x(5, 6, 7))

#3
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

