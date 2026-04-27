def myfunc():
  x = 300
  print(x)

myfunc()


#1
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#2 
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#3
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())