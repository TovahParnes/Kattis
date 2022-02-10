years = int(input())

QALY = 0

for i in range(years):
    line = input()
    q, y = line.split()
    q = float(q)
    y = float(y)
    QALY += q*y


print(QALY)