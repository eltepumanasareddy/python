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