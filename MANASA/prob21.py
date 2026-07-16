def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

#1
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

#2
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

#3
x = lambda a: a + 11
print(x(4))

#4
x = lambda a, b: a * b
print(x(5, 7))

#5
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


