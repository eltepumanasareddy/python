#change tuple values
x=("apple","banana","cherry")
y=list(x)
y[1]="orange"
x=tuple(y)
print(x)

#add items
thislist=("apple","banana","cherry")
y=list(thislist)
y.append("banana")
thistuple=tuple(y)
print(thistuple)

#1
thistuple=("apple","banana","cherry")
y=("cherry",)
thistuple += y
print(thistuple)

#2
thistuple = ("apple","banana","grapes")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)