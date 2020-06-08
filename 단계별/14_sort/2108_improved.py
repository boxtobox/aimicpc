from sys import stdin
ABS_LIMIT = 4000
N = int(stdin.readline())
cnt = [0] * (ABS_LIMIT * 2 + 1)
# key 값이 나타난 빈도. 단, cnt[k]는 k-4000의 빈도임. cnt[0]: -4000의 빈도, cnt[4000]: 0의 빈도, cnt[8000]: 4000의 빈도
result = [0] * 4  # mean, median, mode, range

# 개선: counting sort 사용해서 모든 답 구하기


sum_val = 0
min_val = ABS_LIMIT
max_val = -ABS_LIMIT

for _ in range(N):
    n = int(stdin.readline())
    sum_val += n
    if n < min_val:
        min_val = n
    if n > max_val:
        max_val = n
    cnt[n+ABS_LIMIT] += 1

result[3] = max_val - min_val
result[0] = round(sum_val / N)
max_freq = 1
modes = []
mid_idx = (N+1)/2
sum_freq = 0
found_freq = False

# loop to find median and mode(s)
for i, freq in enumerate(cnt):
    i -= ABS_LIMIT
    if freq > max_freq:
        max_freq = freq
        modes = [i]
    elif freq == max_freq:
        modes.append(i)
    sum_freq += freq
    if not found_freq and sum_freq >= mid_idx:
        result[1] = i
        found_freq = True

if len(modes) == 1:
    result[2] = modes[0]
else:
    result[2] = sorted(modes)[1]

print(*result, sep='\n')

#
# result[0] = round(sum_val / N)
# result[1] =
# result[3] = max_val - min_val
# print(*result, sep='\n')
