#FUNCTION
def my_function(name): 
  print("Hello", name)

my_function("Emil")

#1
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


#2
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")