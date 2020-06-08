from sys import stdin
from operator import itemgetter
read = stdin.readline

N = int(read())
pts = [tuple((map(int, read().split()))) for _ in range(N)]
pts = sorted(pts, key=itemgetter(0, 1))
for p in pts:
    print(*p, sep=' ')
