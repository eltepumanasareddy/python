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




#6
x = range(3, 10, 2)
#display x:
print(x)
#convert to list to display the content of x:
print(list(x))







