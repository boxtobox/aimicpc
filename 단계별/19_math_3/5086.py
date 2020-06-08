def tell(a, b):
    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")


while True:
    j, k = map(int, input().split())
    if j == k == 0:
        break
    tell(j, k)
