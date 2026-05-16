def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

#1
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())
