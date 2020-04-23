import sys

nums = []
for line in sys.stdin:
    nums.append(int(line))

max_num, max_idx = 0, 0
for i in range(len(nums)):
    if nums[i] > max_num:
        max_num = nums[i]
        max_idx = i + 1

print(max_num)
print(max_idx)
