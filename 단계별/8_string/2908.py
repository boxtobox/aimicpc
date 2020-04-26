import sys

nums = tuple(map(int, sys.stdin.readline().split()))
first = (nums[0] % 10) * 100 + (nums[0] // 10 % 10 * 10) + nums[0] // 100
second = (nums[1] % 10) * 100 + (nums[1] // 10 % 10 * 10) + nums[1] // 100
print(max(first, second))
