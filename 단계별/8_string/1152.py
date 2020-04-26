import sys

words = tuple(map(str, sys.stdin.readline().rstrip().split()))
print(len(words))
