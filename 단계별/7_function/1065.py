import sys

N = int(sys.stdin.readline())

def is_hansu(n):
    if n < 100:
        return True
    else:
        a, b = n % 10, (n // 10) % 10
        diff = b - a
        n = n // 10
        while n >= 10:
            a, b = n % 10, (n // 10) % 10
            if b - a != diff:
                return False
            n = n // 10
        return True


result = 0
for i in range(1, N+1):
    if is_hansu(i):
        result += 1

print(result)