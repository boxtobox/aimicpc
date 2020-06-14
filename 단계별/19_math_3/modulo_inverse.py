def extended_gcd(x, y):
    # gcd(x, y) = d = ax + by
    # return (d, a, b)
    assert x >= y
    if y == 0:
        return x, 1, 0
    else:
        d, a, b = extended_gcd(y, x % y)
        return d, b, a - (x//y) * b


n, a = map(int, input().split())
result = extended_gcd(n, a)
if result[0] != 1:
    inv = -1
else:
    inv = result[2]
    while inv < 0:
        inv += n
    # 구한 역원이 음수일 경우, 양수가 될 때까지 m을 더함(mod m)
print(n-a, inv)

# http://stanford.edu/~dntse/classes/cs70_fall09/cs70_fall09_5.pdf
