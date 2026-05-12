x = lambda a: a + 70
print(x(10))

#1
x = lambda a, b : a * b
print(x(2, 6))


#2
x = lambda a, b, c: a + b + c
print(x(10, 12, 16))

#3
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(10)

print(mydoubler(9))


#4
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(6)

print(mytripler(10))

#5
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))










