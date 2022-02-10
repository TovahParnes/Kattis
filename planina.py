pointsEdge = 2

iter = int(input())

for i in range(iter):
    pointsEdge += pointsEdge -1

points = pointsEdge ** 2

print(points)