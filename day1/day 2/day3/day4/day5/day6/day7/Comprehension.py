fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[]
for x in fruits:
    if "c" in x:
        newlist.append(x)
        print(newlist)

#1
fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits if "r" in x]
print(newlist)

