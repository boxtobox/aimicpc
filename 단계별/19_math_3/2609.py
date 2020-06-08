def gcd(a, b):
    # a > b
    while b > 0:
        a, b = b, a % b
    return a


j, k = map(int, input().split())
g = gcd(j, k)
l = j * k // gcd(j, k)
print(g, l)
