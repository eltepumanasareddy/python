print((6+3)-(6-3))
print(100 + 6 * 2)
#left to right
print(5 + 4 - 3 +4)
print(2 + 3 * 4)
print(100 + ~3)
#Bitwise left and right shifts
print(8>>4-2)#Bitwise right shift has a lower precedence than subtraction, and we need to calculate the subtraction first.
#The calculation above reads 8 >> 2 = 2
#More explanation:
#The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.
#Bitwise AND
print(5&3+1)
#bitwise XOR
print(6^2+1)
print(6|2+1)
#==
print(5==4+1)
print(not 5==5)
#AND
print(1 or 2 and 3)
#OR
print(4 or 5 + 10 or 8)

