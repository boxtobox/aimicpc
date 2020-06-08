from math import gcd


def gcd_mult(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result = gcd(result, nums[i])
    return result


def lcm(a, b):
    return a*b//gcd(a, b)


def lcm_mult(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result = lcm(result, nums[i])
    return result

N = int(input())
divisors = tuple(map(int, input().split()))
print(lcm_mult(divisors)*gcd_mult(divisors))