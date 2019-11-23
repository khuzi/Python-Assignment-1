array = [2,1,3,1,3,6,6,2]

print(array)
array.sort()
print(array)

for i in array:
 if array[i] == array[i+1]:
  print(array[i])
 else:
  print("")
