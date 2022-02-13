input = input()
input = input.split(";")

points = 0

for i in range(len(input)):
    if "-" in input[i]:
        range = input[i].split("-")
        points = points + int(range[1]) - int(range[0]) + 1
    else:
        points += 1

print(points)