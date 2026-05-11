x = range(10)
#display x:
print(x)
#convert to list to display the content of x:
print(list(x))

#1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#3
x = lambda a, b: a * b
print(x(5, 6))

