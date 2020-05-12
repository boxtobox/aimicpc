from math import ceil, sqrt
from sys import stdin


def distance(k):
    return int((k + 1) * (k + 1) / 4)


def lt(k):
    return ceil((-1 + sqrt(1+4*k))/2)


N = int(stdin.readline())
for _ in range(N):
    a, b = map(int, stdin.readline().split())
    dist = b - a
    c = lt(dist)
    max_c = distance(2*c - 1)
    if dist <= max_c:
        travels = int(2*c) - 1
    else:
        travels = int(2*c)
    print(travels)
