from sys import stdin

def factorial(k):
    if k <= 1:
        return 1
    else:
        return factorial(k-1) * k

N = int(stdin.readline())
print(factorial(N))
