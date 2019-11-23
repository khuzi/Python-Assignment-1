n = int(input('First Digit:'))
m = int(input('Second Digit:'))

print('1) Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Power')
choice = int(input('Choose operation no.:'))

if choice == 1:
 print( n, "+", m, "=", n + m)
elif choice == 2:
 print( n, "-", m, "=", n - m)
elif choice == 3:
 print( n, "*", m, "=", n * m)
elif choice == 4:
 print( n, "/", m, "=", n / m)
elif choice == 5:
 print( n, "^", m, "=", (pow(n,m)))
else:
 print("Wrong input")



