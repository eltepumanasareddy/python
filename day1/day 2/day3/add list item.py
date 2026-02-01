list=["apple","banana","cherry"]
list.append("orange")#append=always adds an element to the end of a list
print(list)
#1
thislist=["apple","banana","cherry"]
thislist.insert(3,"orange")
print(thislist)
#2
thislist= ["apple","banana","cherry"]
tropical=["mango","papaya","banana"]#tropical list itself is not nested; its elements are merged
thislist.extend(tropical)#extend() adds all elements of one list to another list
print(thislist)
#3
thislist=["apple","banana","cherry"]
thistuple=("kiwi","orange")
thislist.extend(thistuple)
print(thislist)