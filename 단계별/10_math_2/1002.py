from sys import stdin


def dist_sqr(a1, b1, a2, b2):
    return (a1-a2)**2 + (b1-b2)**2


def intersects(x1, y1, r1, x2, y2, r2):
    dist = dist_sqr(x1, y1, x2, y2)
    if dist == 0 and r1 == r2:
        return -1
    elif dist > (r1+r2)**2:
        return 0
    elif dist < (r1-r2)**2:
        return 0
    elif dist == (r1+r2)**2:
        return 1
    elif dist == (r1-r2)**2:
        return 1
    elif (r1-r2)**2 < dist < (r1+r2)**2:
        return 2


N = int(stdin.readline())
for _ in range(N):
    data = map(int, stdin.readline().split())
    print(intersects(*data))

