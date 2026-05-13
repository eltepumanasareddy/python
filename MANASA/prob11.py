x = range(10)
#display x:
print(x)
#convert to list to display the content of x:
print(list(x))

#1
x = range(3, 10)
#display x:
print(x)
#convert to list to display the content of x:
print(list(x))

#2
def countdown(n):
  if n <= 5:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)
