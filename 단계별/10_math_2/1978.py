from sys import stdin
from math import floor, sqrt

MAX = 1000
c = floor(sqrt(MAX))
prime1 = [2, 3]
for i in range(4, c+1):
    for j in prime1:
        if i % j == 0:
            break
    else:
        prime1.append(i)

prime2 = []
for i in range(prime1[-1] + 1, MAX+1):
    for j in prime1:
        if i % j == 0:
            break
    else:
        prime2.append(i)

primes = prime1 + prime2

N = int(stdin.readline())
inputs = list(map(int, stdin.readline().split()))
prime_count = [i for i in inputs if i in primes]
print(len(prime_count))
