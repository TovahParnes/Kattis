text = input()
split = text.split()
split = list(map(int, split))

points = int(input())

if (points >= split[0]):
    print("A")
elif (points >= split[1]):
    print("B")
elif (points >= split[2]):
    print("C")
elif (points >= split[3]):
    print("D")
elif (points >= split[4]):
    print("E")
else:
    print("F")
