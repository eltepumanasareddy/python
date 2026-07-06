#1
def my_function(a, b, /, *,c,d):
    return a+b+c+d
result = my_function(5,10, c=15,d=20)
print(result)

#2
def my_function(*kids):
    print("The youngest child is " +kids[2])
my_function("Emil","Tobias", "Linus")