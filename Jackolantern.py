nums = input()
nums = nums.split()

sum = 1

for i in range(len(nums)):
    sum *= int(nums[i])

print(sum)