from sys import stdin

cache = {}


def res(k, n) -> int:
    key = (k, n)
    global cache
    if key in cache:
        return cache[key]
    else:
        if k == 0:
            cache[key] = n
            return n
        elif n == 1:
            cache[key] = 1
            return 1
        else:
            cache[key] = res(k, n-1) + res(k-1, n)
            return cache[key]


N = int(stdin.readline())
for _ in range(N):
    K = int(stdin.readline())
    N = int(stdin.readline())
    print(res(K, N))
