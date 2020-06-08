def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def fraction(a, b):
    print('%d/%d' % (a//gcd(a, b), b//gcd(a, b)))
    return


N = int(input())
nums = list(map(int, input().split()))
for i in range(1, len(nums)):
    fraction(nums[0], nums[i])
