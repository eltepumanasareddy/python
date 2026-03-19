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


#6
score=90
extra_credit = 5
if score >=85:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >=80:
  print("B grade")
else:
  print("C grade or below")



#pass
a=10
b=20
if a>b:
  pass


age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")


score = 45

if score > 80:
  pass # This is excellent
print("Score processed")


value = 40

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")




