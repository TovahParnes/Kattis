import math 

line = input()
n, w, h = line.split()
n = int(n)
w = int(w)
h = int(h)

for i in range(n):
    length = int(input())
    if (length <= math.sqrt(w*w+h*h)):
        print("DA")
    else:
        print("NE")