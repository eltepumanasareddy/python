myfamily={
    "child1":{
        "name":"Emil",
        "year":2005
    },
    "child2":{
        "name" : "Tobias",
    "year" : 1990
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2001
  }
}
print(myfamily["child2"]["name"])

#1
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2007
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2002
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2016
  }
}
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])

