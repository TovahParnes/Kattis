import math

line = input()
n, k = line.split()
n = int(n)
k = int(k)

knownRating = 0

for i in range(k):
    knownRating += int(input())

min = ((n-k)*(-3)+knownRating)/n
max = ((n-k)*(3)+knownRating)/n

print(str(min) + " " + str(max))