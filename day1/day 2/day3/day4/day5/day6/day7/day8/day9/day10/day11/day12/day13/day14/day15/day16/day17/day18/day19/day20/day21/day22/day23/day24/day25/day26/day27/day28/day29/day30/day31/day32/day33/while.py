i = 1
while i < 6:
  print(i)
  i += 1


#1
i = 1
while i < 4:
  print(i)
  if i == 3:
    break
  i += 1

#2
i = 0
while i < 5:
  i += 1
  if i == 4:
    continue
  print(i)


#3
i=1
while i < 5:
  print(i)
else:
  print("i is no longer less than 8")
