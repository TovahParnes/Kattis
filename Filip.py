text = input()
split = text.split()
split = list(map(int, split))

new = []
for j in range(len(split)):
    num = 0
    current = split[j]
    for i in range(len(str(split[j]))):
        length = len(str(split[j]))
        num += (current%(10)) * (10 ** (length - i-1))
        current = current//10
    new.append(num)

print(max(new))
