cases  = int(input())


for i in range(cases):
    text = input()
    split = text.split()
    split = list(map(int, split))
    sum = 1-split[0]
    for i in range(1, len(split)):
        sum+= split[i]
    print(sum)