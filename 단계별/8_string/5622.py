import sys

nums = str(sys.stdin.readline().rstrip()).lower()
dials = {'abc': 2, 'def': 3, 'ghi': 4, 'jkl': 5, 'mno': 6 , 'pqrs': 7, 'tuv': 8, 'wxyz': 9}
result = 0
for num in nums:
    for k, v in dials.items():
        if num in k:
            result += v + 1

print(result)
