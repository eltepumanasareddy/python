#boolean
#print(4<5)
#print(4>5)
#print(4==5)
#print(4==4)

#if statement
#a=200
#b=199
#if b>a:
   # print("b is greater than a")
#else:
 #   print("b is not greater than a")

#evaluate a string and a number:
#print(bool("hello"))
#print(bool(16))

#evaluate two variables:
#x="manasa"
#y=16
#print(bool(x))
#print(bool(y))

# values are true
#bool("dhgjs")
#bool(12345)
#bool(["apple","banana","cherry"])

# flase statement
bool(False)
bool(0)
bool("")
bool(())
bool([])
bool({})

def Myfunction() :
  return True

print(Myfunction())

#return sends a value back to the caller
 #Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

 if myFunction():
  print("YES!")
 else:
  print("NO!")

  
  #isinstance(.)
 x = 200
print=(isinstance(x,int)) #(object,type)

 #Check if "Hello" is one of the types described in the type parameter:
x= isinstance("hello",(float,int,str,list,dict,tuple))
print(x)
