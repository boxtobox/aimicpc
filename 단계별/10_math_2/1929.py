from sys import stdin

M, N = map(int, stdin.readline().split())

length = int(N**0.5)
sieve = [1] * (N+1)
sieve[0:2] = 0, 0

for i in range(2, length + 1):
    if sieve[i]:
        sieve[i*2::i] = [0] * (N // i - 1)

print('\n'.join([f'{i}' for i in range(M, N+1) if sieve[i]]))


# https://www.acmicpc.net/source/19928190
