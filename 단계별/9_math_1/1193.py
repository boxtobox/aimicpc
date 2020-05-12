import sys
from math import sqrt, ceil

N = int(sys.stdin.readline())


def quadratic_eq(n):  # problem-specific function. must NOT generally use.
    a, b, c = 1, 1, -2*n
    return (b * (-1) + sqrt(b * b - 4 * a * c)) / (2 * a)


k = ceil(quadratic_eq(N))
order = int(N - k*(k-1)/2)

if k % 2:
    print(f'{k+1-order}/{order}')
else:
    print(f'{order}/{k+1-order}')
