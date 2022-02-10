cost = float(input())
lawns = int(input())

area = 0

for i in range(lawns):
    text = input()
    split = text.split()
    split = list(map(float, split))

    area += split[0]*split[1]

print(area*cost)