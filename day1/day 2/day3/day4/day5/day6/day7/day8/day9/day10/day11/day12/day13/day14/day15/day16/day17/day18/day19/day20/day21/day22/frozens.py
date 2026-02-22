#frozenset is a Once created, you cannot add or remove items.
x=frozenset({"apple","banana","cherry"})
print(x)
print(type(x))

#1
fs = frozenset({1,2,3})
cp=fs.copy()
print(fs)
print(cp)
#2
a=frozenset({1,2})
b=frozenset({3,4})
c=frozenset({2,5})
print(a.isdisjoint(b))
print(a.isdisjoint(c))

#3
a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)

#4
thisdict={
    "brand": "Ford","model":"Mustang","year":2005
}
print(thisdict)

#5
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#6
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(dict)

#7
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(type(dict))

#8
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(dict))

#9
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 



