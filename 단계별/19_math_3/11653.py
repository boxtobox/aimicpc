def find_primes(limit):
    """
    에라토스테네스의 체. 길이가 limit+1인 리스트를 리턴한다.
    만약 i가 소수이면, limit[i] = 1이고, 그렇지 않으면 limit[i] = 0이다.
    """
    length = int(limit ** 0.5)
    sieve = [1] * (limit + 1)
    sieve[0:2] = 0, 0
    for i in range(2, length + 1):
        if sieve[i]:
            sieve[i * 2::i] = [0] * (limit // i - 1)
    return sieve


LIMIT = 10000000
primes = find_primes(LIMIT)
N = int(input())
for i in range(len(primes)+1):
    if primes[i]:
        while N % i == 0:
            print(i)
            N //= i
        if N == 1:
            break


