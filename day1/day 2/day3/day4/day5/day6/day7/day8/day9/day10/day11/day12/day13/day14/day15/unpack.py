fruits = ("apple", "banana", "cherry")
print(fruits)

#1
fruits = ("apple", "banana", "cherry")
(blue, yellow, red) = fruits
print(blue)
print(yellow)
print(red)

#2
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(blue, yellow, *red) = fruits
print(blue)
print(yellow)
print(red)

