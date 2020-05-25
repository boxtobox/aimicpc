from sys import stdin

N, M = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))
cards.sort(reverse=True)


def findsum(cards, goal):
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                S = cards[i] + cards[j] + cards[k]
                if S < result:
                    break
                if goal >= S > result:
                    result = S
    return result


def findsum2(cards, goal):
    temp_result = []
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                S = cards[i] + cards[j] + cards[k]
                print(S, end=' ')


print(findsum(cards, M))


'''루프 중간에 끝내버릴 수 있는 조건이 있는가?
    1) 3번째 inner loop 돌 때는 항상 다음 루프의 값이 앞선 루프의 값보다 작으므로, 합계는 점점 작아진다. 
    따라서, 세 값의 합계가 /현재 구한 /조건에 맞는 합계/보다 더 작은 경우에는, 3번째 inner loop는 종료해도 됨.
    
    카드를 큰 순서로 정렬하지 않고, 작은 순서로 정렬한다면? ?????????????????????????
    
'''
