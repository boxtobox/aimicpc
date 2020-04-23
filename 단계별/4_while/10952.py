import sys

a, b = map(int, sys.stdin.readline().split())

while a or b:
    print(a + b)
    a, b = map(int, sys.stdin.readline().split())