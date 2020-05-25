from sys import stdin


'''
    N의 분해합이 M이면, N은 M의 생성자이다.
    
자연수 M의 생성자는..   
    2) M보다 작다
    3) M의 자릿수가 k인데, 생성자가 (k-2) 자릿수가 되는것은 불가능해.
    4) M의 자릿수가 k인데, 생성자가 (k-1) 자릿수가 되려면, M의 가장 큰 자릿수 숫자가 1이여야 함.
    M의 가장 높은 자릿수의 숫자를 a라 했을 때, 
     - 1]] 생성자의 가장 높은 자릿수의 숫자도 a라면, 생성자는 M-(a+9*(k-1))보다 크거나 같아야 한다.
     - 2]] 생성자의 가장 높은 자릿수의 숫자가 a-1이라면, 생성자는 M
    

'''
def break_sum(k):
    result = k
    while k > 0:
        result += k % 10
        k //= 10
    return result


results = []
duplicates = {}
for i in range(0, 1101):
    n = break_sum(i)
    if n not in results:
        results.append(n)
    else:
        duplicates[n] += [i]
    print(i, n, n - i)

print(duplicates)