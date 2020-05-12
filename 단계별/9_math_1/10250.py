from sys import stdin
from math import ceil

N = int(stdin.readline())
for _ in range(N):
    H, W, N = map(int, stdin.readline().split())
    w = ceil(N/H)

    if N % H:
        h = N % H
    else:
        h = H

    roomname = h * 100 + w
    print(roomname)

