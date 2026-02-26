myfamily={
    "child1":{
    "name":"Email",
    "year":2005
},
"child2":{
    "name":"manasa",
    "year":2007
},
"child3":{
    "name":"sathvika",
    "year":2008
}
}
print(myfamily)

#1
child1={
    "name":"Email",
    "year":2005
}
child2={
    "name":"manasa",
    "year":2006
}
child3={
    "name":"vinay",
    "year":2006
}
myfamily={
 "child1":child1,
 "child2":child2,
 "child3":child3
}
print(myfamily)

#2
myfamily = {
  "child1" : {
    "name" : "Email",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])