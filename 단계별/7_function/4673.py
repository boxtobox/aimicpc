def d(n):
    result = n
    while n > 0:
        result += n % 10
        n = n // 10
    return result

self_nums = list(range(1, 10001))


for i in range(1, 10001):
    if d(i) in self_nums:
        self_nums.remove(d(i))

for number in self_nums:
    print(number)