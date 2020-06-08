from sys import stdin
# counting sort
LIMIT = 10000


def counting_sort(arr):
    cnt = dict()
    for num in arr:
        if num not in cnt:
            cnt[num] = 1
        else:
            cnt[num] += 1
    return cnt


N = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(N)]
cnt_dict = counting_sort(arr)
for i in range(LIMIT):
    if i in cnt_dict:
        for _ in range(cnt_dict[i]):
            print(i)
