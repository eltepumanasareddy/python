def myfun(n):
    return abs(n - 50)
thislist=[100,50,60,82,40]
thislist.sort(key = myfun)
print(thislist)

#1
thislist=["banana","orange","kiwi","cherry"]
thislist.sort()
print(thislist)