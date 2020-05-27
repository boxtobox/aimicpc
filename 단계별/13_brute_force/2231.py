from sys import stdin


def break_sum(k):
    result = k
    while k > 0:
        result += k % 10
        k //= 10
    return result


N = stdin.readline().rstrip()
digit = len(N)
N = int(N)

for i in range(N - digit*9, N):
    if break_sum(i) == N:
        result = i
        break
    result = 0
print(result)



# LIMIT = 1000000
# gen_list = [0] * (LIMIT+1)
# for i in range(1, LIMIT+1):
#     br_sum = break_sum(i)
#     if br_sum <= LIMIT:
#         if gen_list[br_sum]:
#             if i < gen_list[br_sum]:
#                 gen_list[br_sum] = i
#         else:
#             gen_list[br_sum] = i
#
# N = int(stdin.readline())
# print(gen_list[N])

'''
    N의 분해합이 M이면, N은 M의 생성자이다.

자연수 M의 생성자는..   
    2) M보다 작다
    3) M의 자릿수가 k인데, 생성자가 (k-2) 자릿수가 되는것은 불가능해.
    4) M의 자릿수가 k인데, 생성자가 (k-1) 자릿수가 되려면, M의 가장 큰 자릿수 숫자가 1이여야 함.
    M의 가장 높은 자릿수의 숫자를 a라 했을 때, 
     - 1]] 생성자의 가장 높은 자릿수의 숫자도 a라면, 생성자는 M-(a+9*(k-1))보다 크거나 같아야 한다.
     - 2]] 생성자의 가장 높은 자릿수의 숫자가 a-1이라면, 생성자는 M
    A -> (분해합) -> B이면, A는 B의 생성자.
    언제나 A < B


'''

'''
1번째 방법: N의 생성자는 항상 N보다 작으므로, limit까지의 분해합을 모두 구해서, 
생성자와 대응 관계를 저장

2번째 방법: N의 생성자가 될 수 있는 범위를 지정해서, 그 범위 내에서만 찾아본다.
N의 자릿수: k일 때, 
만약, 최고자릿수가 같다면, 최대 9*(k-1)의 차이가 있을 수 있다.
최고 자릿수가 1 차이가 난다면,   

'''