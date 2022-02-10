text = input()
split = text.split()
split = list(map(int, split))

new = []
for j in range(len(split)):
    num = 0
    for i in range(len(str(split[j]))):
        length = len(str(split[j]))
        current = split[j]
        print((current%(10)))
        num += (current%(10 ** i)) * (10 ** (length - i))
        current = int(current/10)
    new.append(num)

print(max(new))
