text = input()
split = text.split()
split = list(map(int, split))

a = split[0]*(split[1]-1) + 1
print(a)