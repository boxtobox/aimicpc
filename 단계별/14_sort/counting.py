from sys import stdin
LIMIT = 10000
cnt = [0] * (LIMIT+1)

N = int(stdin.readline())
for _ in range(N):
    cnt[int(stdin.readline())] += 1

for num, c in enumerate(cnt):
    if c:
        print(*([num]*c), sep='\n')
