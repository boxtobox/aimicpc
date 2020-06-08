from sys import stdin
from operator import itemgetter
ABS_LIMIT = 4000
N = int(stdin.readline())
arr = []
cnt = dict()
result = [0] * 4  # mean, median, mode, range


def counter(k):
    if k < 0:
        k = ABS_LIMIT - k
    if k in cnt:
        cnt[k] += 1
    else:
        cnt[k] = 1


for _ in range(N):
    n = int(stdin.readline())
    arr.append(n)
    counter(n)
arr.sort()
result[0] = round(sum(arr) / N)
result[1] = arr[N//2]
result[3] = arr[-1] - arr[0]

sorted_cnt = sorted(cnt.items(), key=itemgetter(1), reverse=True)
modes = []
mode = sorted_cnt[0][1]
for num in sorted_cnt:
    if num[1] != mode:
        break
    if num[0] > ABS_LIMIT:
        val = ABS_LIMIT - num[0]
    else:
        val = num[0]
    modes.append(val)

if len(modes) > 1:
    result[2] = sorted(modes)[1]
else:
    result[2] = modes[0]

print(*result, sep='\n')
