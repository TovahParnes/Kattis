num = int(input())

sum = 0

for i in range(num):
    a = int(input())
    p = int(a/10)
    exp = a%10
    sum += p ** (exp)

print(sum)