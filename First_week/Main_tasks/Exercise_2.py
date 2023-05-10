import sys

num = int(sys.argv[1])
s = " "
d = "#"
c = 1
while num > 0:
    print(s*(num-1), "#"*c, sep = "")
    num = num-1
    c = c+1

