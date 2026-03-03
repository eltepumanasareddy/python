a=200
b=50
if b>a:
    print("b is greater than a")
elif b<a:
    print("b is greater than a")
else:
    print("a is greater than a")

#1
a=200
b=400
if a>b:
    print("a is greater than a")
else:
    print("b is greater than a")

#2
number=8
if number%2==0:
    print("the number is even")
else:
    print("the number is odd")

#3
temperature=30
if temperature > 40:
    print("its a cool")
elif temperature >30:
    print("its a warm")
elif temperature >10:
    print("its a hot")
else:
    print("its a cool inside")

#4
username="Email"
if len(username)>0:
    print(f"welcome,{username}!")
else:
    print("Error:username cannot be empty")
    