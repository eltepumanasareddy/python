#AND
# print(6 & 3)#sets each bit to 1 if both bits are 1	
#6 = 0000000000000110
#3 = 0000000000000011
#--------------------
#2 = 0000000000000010

#OR
print(6 | 4)#Sets each bit to 1 if one of two bits is 1
#6 = 0000000000000110
#3 = 0000000000000011
#--------------------
#7 = 0000000000000111

#XOR
print(6 ^ 4)
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101

#NOT
print(~4)

#x<<2
#Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(3<<4)