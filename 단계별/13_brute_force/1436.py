
'''
666

[0~9] <- '666'
[00~99] <- '666'
[000~999] <- '666'
[0000~9999] <- '6666'
--> 직관적으로 이해가 잘 안돼서 이해하려고..
'''


from sys import stdin
devil_n = {666}
for k in range(1, 5):
    for num in range(0, 10**k):
        for pos in range(0, k+1):
            new_num = int(str(num).zfill(k)[:pos] + '666' + str(num).zfill(k)[pos:])
            devil_n.add(new_num)

devil_n = list(devil_n)
devil_n.sort()

N = int(stdin.readline())
print(devil_n[N-1])

# 느린 버전
# devil_n_bf = [666]
#
# k = 667
# N = 1
#
# while N < 10000:
#     if '666' in str(k):
#         devil_n_bf.append(k)
#         N += 1
#     k += 1
#
# for i in range(10000):
#     if devil_n[i] != devil_n_bf[i]:
#         print(i, devil_n[i], devil_n_bf[i])