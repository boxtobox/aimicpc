from sys import stdin


def bertrand(n):
    sieve = [1] * (2*N+1)
    sieve[0:2] = 0, 0

    for i in range(2, int((2*n)**0.5) + 1):
        if sieve[i]:
            sieve[i*2::i] = [0] * (2*n // i - 1)

    primes = [i for i in range(n+1, 2*n+1) if sieve[i]]
    return len(primes)


while True:
    N = int(stdin.readline())
    if not N:
        break
    print(bertrand(N))
