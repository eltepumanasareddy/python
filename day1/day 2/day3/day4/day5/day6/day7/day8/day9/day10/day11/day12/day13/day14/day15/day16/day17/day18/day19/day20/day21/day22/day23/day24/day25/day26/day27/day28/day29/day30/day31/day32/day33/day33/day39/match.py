day = 6
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")


#1
day = 5
match day:
    case 6:
       print("Today is saturday")
    case 7:
        print("Today is sunday")
    case 8:
        print("Looking forward to the weekend")


#2
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")


#3
day = 1
match day:
    case 2:
       print("Today is monday")
    case 3:
        print("Today is tuesday")
    case 4:
        print("Looking forward to the weekend")

