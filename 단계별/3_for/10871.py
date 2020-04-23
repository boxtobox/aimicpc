import sys
N, X = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
assert(len(nums) == N)
[print(num, end=' ') for num in nums if num < X]