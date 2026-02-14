thistuple=("apple","banana","cherry")
for x in thistuple:
    print(x)

#1
thistuple=("apple","banana","cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

#2
thistuple=("apple","banana","cherry")
i=0
while i<len(thistuple):
    print(thistuple[i])
    i=i+1

#3
thistuple1=("a","b","c")
thistuple2=(1,2,3)
thistuple3=thistuple1+thistuple2
print(thistuple3)

#4
fruits=("apple","banana","cherry")
mytuple=fruits*2
print(mytuple)
