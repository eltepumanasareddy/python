#1
for x in range(6):
    print(x)
else:
    print("finished")

#2
def my_function():
    print("hello the my function")
my_function()

#3 Arguments
def my_function(fname):
    print(fname + " References")
my_function("Email")
my_function("Tobias")
my_function("Linus")

#4
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Reference")

#5
def my_function(name= "friend"):
    print("Hello", name)
my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#6
def my_function(animal,name):
    print("I have a", animal)
    print("My",animal + "'s name is",name)
my_function(animal="dog",name = "Buddy")

#7
def my_function(animal,name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
my_function("dog", "buddy")

#8
def my_function(animal,name,age):
    print("I have a", age,"year old", animal,"named", name)
my_function("dog", name = "buddy", age=5)

#9
def my_function(fruits):
    for fruits in fruits:
     print(fruits)
my_fruits = ["apple","banana","cherry"]
my_function(my_fruits)

#10
def my_function(x,y):
    return x + y
result = my_function(5,3)
print(result)

#11
def my_function():
    return["apple","banana","cherry"]
fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#12
def my_function():
  return (10, 20)
x, y = my_function()
print("x:", x)
print("y:", y)

#13
def my_function(name):
  print("Hello", name)

my_function("Emil")

#14
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 12, c = 15, d = 20)
print(result)

#15
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

#16
def my_function(name):
  print("Hello", name)

my_function("Emil")

