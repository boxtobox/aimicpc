from sys import stdin


def chk_in_circle(x, y, cx, cy, r):
    if (x - cx) ** 2 + (y - cy) ** 2 < r**2:
        return True
    else:
        return False


N = int(stdin.readline())
for _ in range(N):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    systems = int(stdin.readline())
    count = 0
    for _ in range(systems):
        cx, cy, r = map(int, stdin.readline().split())
        count += chk_in_circle(x1, y1, cx, cy, r) ^ chk_in_circle(x2, y2, cx, cy, r)
    print(count)
