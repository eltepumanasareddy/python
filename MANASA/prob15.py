def myfunc():
  x = 100
  print(x)

myfunc()

#1
def myfunc():
  x = 100
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#2
x = 500

def myfunc():
  print(x)

myfunc()

print(x)

#3
def myfunc1():
  x = "john"
  def myfunc2():
    nonlocal x
    x = "boss"
  myfunc2()
  return x

print(myfunc1())

#4
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

#1
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#2
