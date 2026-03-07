list1=["a","b","c"]
list2=[4,5,6]
list3=list1 + list2
print(list3)

#1
list1=["a","b","c",]
list2=[4,5,6]
for x in list2:
    list1.append(x)
print(list1)

#2
list1=["a","b","c",]
list2=[2,3,4]
list1.extend(list2)
print(list1)