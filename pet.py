winNum = 0
maxPoint = 0

for i in range(5):
    line = input()
    a, b, c, d = line.split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    sumPoints = a+b+c+d
    if (sumPoints > maxPoint):
        winNum = i+1
        maxPoint = sumPoints

print ( str(winNum) + " " + str(maxPoint))