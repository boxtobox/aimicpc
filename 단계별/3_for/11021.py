import sys
N = int(sys.stdin.readline())
for i in range(N):
    a, b = map(int, input().split())
    print(f'Case #{i + 1}: {a + b}')