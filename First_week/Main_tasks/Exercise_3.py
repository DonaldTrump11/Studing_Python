import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b**2 - 4*a*c
D = D**0.5

x_1 = (-b +D)/(2*a)
x_2 = (-b -D)/(2*a)

print(int(x_1))
print(int(x_2))
