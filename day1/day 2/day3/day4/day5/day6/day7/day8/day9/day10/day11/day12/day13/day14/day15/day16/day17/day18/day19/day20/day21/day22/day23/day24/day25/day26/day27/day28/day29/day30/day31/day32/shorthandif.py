a=225
b=45
if a > b:  print("a is greater than b")

#1
a=21
b=20
print("A") if a > b else print("B")

#2
a=20
b=30
bigger = a if a>b else b
print("bigger is",bigger)


#3
a=60
b=60
print("A") if a>b else print("=") if a==b else print("B")


#4
x=50
y=40
max_value = x if x > y else y
print("Maximum value:",max_value)

#5
a=40
b=50
c=500
if a > c and b<a:
    print("Both conditions are True")

a=44
b=50
if not a>b:
    print("a is Not greater than b")