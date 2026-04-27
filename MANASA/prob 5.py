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