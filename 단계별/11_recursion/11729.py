from sys import stdin
hanoi_move_list = [0] * 21


def hanoi_moves(n):
    if hanoi_move_list[n]:
        return hanoi_move_list[n]
    elif n == 1:
        hanoi_move_list[n] = 1
        return 1
    else:
        result = 2 * hanoi_moves(n - 1) + 1
        hanoi_move_list[n] = result
        return result


def move(start, dest):
    print(f"{start} {dest}")


def hanoi_process(start, dest, n):
    if n == 1:
        move(start, dest)

    else:
        rest = ({1, 2, 3} - {start, dest}).pop()
        hanoi_process(start, rest, n-1)
        move(start, dest)
        hanoi_process(rest, dest, n-1)
        return


# N = int(stdin.readline())
# print(hanoi_moves(N))
# hanoi_process(1, 3, N)
for i in range(1, 11):
    print(hanoi_moves(i))
# 언제나 첫번째 고리에서 세번째 고리로 링들을 전부 옮기는 것이 목표임
# 고리 종류: start, dest, rest
'''start 고리에서 rest 고리로 맨 아랫 링을 제외한 링들을 옮기고,
    start번째 고리에서 dest 고리로 맨 아랫 링을 옮기고
    rest번째 고리에서 dest번째 고리로  맨 아랫 링을 제외한 링들을 옮김.
    rest가 몇번째 고리인지 구함.
    1, 3 -> 2
    1, 2 -> 3
    2, 3 -> 1
    차집합
'''
