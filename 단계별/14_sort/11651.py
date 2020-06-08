from sys import stdin, stdout
from operator import itemgetter
read = stdin.readline

N = int(read())
pts = [tuple((map(int, read().split()))) for _ in range(N)]
pts = sorted(pts, key=itemgetter(1, 0))
# pts = sorted(pts, key=lambda k: (k[1], k[0]))
# for x, y in pts:
#     stdout.write(f'{x} {y}\n')

stdout.write('\n'.join(f'{x} {y}' for x, y in pts))
