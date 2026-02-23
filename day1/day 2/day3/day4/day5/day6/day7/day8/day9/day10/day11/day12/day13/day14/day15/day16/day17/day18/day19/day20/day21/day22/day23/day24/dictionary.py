car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.values()#before the change
print(x)
car["year"]=2020#after the change
print(x)

#1
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change
