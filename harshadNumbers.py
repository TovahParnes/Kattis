firstNum = int(input())

sum = firstNum+1

while (True):
    num = firstNum
    sum = 0
    while (num > 0):
        sum += num%10
        num = int(num/10)

    if (firstNum%sum == 0):
        break

    firstNum += 1

print(firstNum)

