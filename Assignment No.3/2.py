list = ['Robert',1,'Tommy',50,'twelve']

intType = type(2)

for i in list:
 if type(i) == intType:
  print("There is a numeric Value:", i)
 else:
  print(i, "is not a numeric value")

