fruits=["apple","banana","kiwi","guva"]
newlist=[x.upper() for x in fruits]
print(newlist)

#1
fruits=["apple","banana","kiwi","guva"]
newlist=['hello' for x in fruits]
print(newlist)

#2
fruits=["apple","banana","kiwi","guva"]
newlist=[x if x!="banana" else "orange" for x in fruits]
print(newlist)

