#x = "awesome"

#def myfunc():
  #print("Python is " + x)

#myfunc()


#create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
