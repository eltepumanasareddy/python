fruits = ["apple","banana","grapes"]
for x in fruits:
    print(x)
    if x == "banana":
       break


fruits= ["apple","banana","grapes"]
for x in fruits:
    if x == "grapes":
        break
    print(x)


fruits = ["apple","banana","cherry"]
for x in fruits:
    if x=="cherry":
        continue
    print(x)


for x in range(5):
    print(x)

for x in range(2,6):
    print(x)


#range
for x in range(3,30,5):
    print(x)


for x in range(6):
    print(x)
else:
    print("Finally finished!")


for x in range(6):
    if x==4: break
    print(x)
else:
    print("Finally finished!")


adj=["red","green","blue"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

 
for x in[0,1,2]:
    pass



#function
def my_function():
    print("Hello from a function")
my_function()