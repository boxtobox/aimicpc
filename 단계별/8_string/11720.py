import sys

N = int(sys.stdin.readline())

input = str(sys.stdin.readline().rstrip())

assert(len(input) == N)

result = 0
for number in input:
    result += int(number)

print(result)