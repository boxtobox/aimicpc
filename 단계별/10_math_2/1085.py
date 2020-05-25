from sys import stdin

x, y, w, h = map(int, stdin.readline().split())
print(min(min(x, w-x), min(y, h-y)))
