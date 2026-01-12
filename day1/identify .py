x=["apple","banana"]
y=["apple","banana"]#y is another list with the same values, but it is a different list in memory
z=x#z = x means z points to the same list as x
print(x is y)
print(x == y)
print(x is z)

#1
x=["apple","banana"]
y=["apple","banana"]
z=x
print(x is not y)
print(x==y)
print(x==z)#values equal
print(x!=y)#same value thats why true will be come
print(x is not z)## returns False because z is the same object as x

#2
x=[1,2,3,4]
y=[1,2,3,4]
print(x is y)#is → same person
print(x == y)#== → same clothes
 #if two variables point to the same object             