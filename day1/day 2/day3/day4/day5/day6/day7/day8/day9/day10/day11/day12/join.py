list1=["a","b","c"]
list2=[3,2,5]
list3=list1 + list2
print(list3)

#1
list1=["a","b","c",]
list2=[3,2,1]
for x in list2:
    list1.append(x)
print(list1)

#2
list1=["a","b","c",]
list2=[3,2,1]
list1.extend(list2)
print(list1)