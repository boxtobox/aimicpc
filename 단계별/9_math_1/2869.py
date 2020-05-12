import sys
from math import ceil

a, b, v = map(int, sys.stdin.readline().split())
print(ceil((v-a) / (a-b)) + 1)
