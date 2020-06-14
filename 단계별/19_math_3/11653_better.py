# 에라토스테네스의 체를 사용하지 않고 구하는 것이 더 빠르다

N = int(input())
m = 2
factors = []

while N % 2 == 0:
    factors.append(m)
    N //= m

m += 1
while N > 1 and m*m <= N:
    while N % m == 0:
        factors.append(m)
        N //= m
    m += 2

if N > 1:
    factors.append(N)

print(*factors, sep='\n')