from sys import stdin
from math import gcd


def gcd_nums(nums):
    result = nums[0]
    for num in nums:
        result = gcd(result, num)
    return result

def divisors(factors):
    """
    Generates all divisors, unordered, from the prime factorization.
    """
    ps = sorted(set(factors))
    print(ps)
    omega = len(ps)

    def rec_gen(n=0):
        if n == omega:
            yield 1
        else:
            pows = [1]
            for j in range(factors.count(ps[n])):
                pows += [pows[-1] * ps[n]]
            for q in rec_gen(n + 1):
                for p in pows:
                    yield p * q

    for p in rec_gen():
        yield p


a = [div for div in divisors([2, 2, 2, 3, 3, 5])]
print(a)
a.remove(1)
a = sorted(a)
print(a)


