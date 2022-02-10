n = int(input())

for i in range(n):
    text = input()
    split = text.split()
    split = list(map(int, split))
    

    if (split[0] + split[2] < split[1]):
        print("advertise")
    elif(split[0] + split[2] == split[1]):
        print("does not matter")
    else:
        print("do not advertise")