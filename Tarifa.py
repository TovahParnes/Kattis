megabytes = int(input())
months = int(input())
left = megabytes*(months+1)

for i in range(months):
    left = left-int(input())

print(left)