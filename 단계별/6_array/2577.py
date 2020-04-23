import sys

nums = []
for line in sys.stdin:
    nums.append(int(line))

product = 1
for i in nums:
    product *= i

result = [0] * 10

for i in str(product):
    result[int(i)] += 1

for i in result:
    print(i)