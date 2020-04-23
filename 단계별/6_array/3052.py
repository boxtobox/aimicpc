import sys

nums = []
for line in sys.stdin:
    nums.append(int(line))

remainders = set()
for num in nums:
    remainders.add(num % 42)

print(len(remainders))