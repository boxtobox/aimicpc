import sys

N = int(sys.stdin.readline())
strings = []

for _ in range(N):
    repeat, string = map(str, sys.stdin.readline().rstrip().split())
    repeat = int(repeat)
    strings.append((repeat, string))

for item in strings:
    for ch in item[1]:
        repeat = item[0]
        print(ch * repeat, end='')
    print()
