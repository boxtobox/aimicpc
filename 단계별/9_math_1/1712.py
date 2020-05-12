import sys
from math import floor

fc, vc, p = map(int, sys.stdin.readline().split())

if vc >= p:
    bep = -1
else:
    bep = floor(fc / (p - vc)) + 1

print(bep)
