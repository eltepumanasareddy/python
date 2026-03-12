x= 40
if x>10:
 print("Above ten",)
 if x>20:
  print("and also above 20!")
 else:
  print("but not above 20.")


  #1
 age = 25
 has_license = True

if age>= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")


#2
score = 65
attendence = 90
submitted=True

if score >= 60:
  if attendence >= 80:
    if submitted:
      print("pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")


#3
temperature = 25
is_sunny = True
if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

#4
temperature = 30
is_sunny = True
if temperature > 25 and is_sunny:
    print("perfect beach weather!")


#5
username = "email"
password = "python12"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
       print("password required")
else:
        print("Username required")
        

