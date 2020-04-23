import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
assert(len(nums) == N)

max_num = nums[0]
min_num = nums[0]
for num in nums[1:]:
    if max_num < num:
        max_num = num
    elif min_num > num:
        min_num = num

print(min_num, max_num)