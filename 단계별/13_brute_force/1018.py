from sys import stdin


def cnt_diff_str(str_a, str_b):
    cnt = 0
    assert len(str_a) == len(str_b)
    for i in range(0, 8):
        if str_a[i] != str_b[i]:
            cnt += 1
    return cnt


def cnt_diff_mat(mat_8x8):
    assert len(mat_8x8) == 8
    B = 'BWBWBWBW'
    W = 'WBWBWBWB'
    diff_b, diff_w = 0, 0
    for i in range(0, 8, 2):
        diff_b += cnt_diff_str(mat_8x8[i], B)
        diff_w += cnt_diff_str(mat_8x8[i], W)
    for i in range(1, 8, 2):
        diff_w += cnt_diff_str(mat_8x8[i], B)
        diff_b += cnt_diff_str(mat_8x8[i], W)
    return min(diff_b, diff_w)


M, N = map(int, stdin.readline().split())
data = []
for i in range(M):
    data.append(stdin.readline().rstrip())

result = 64
for i in range(0, M-8+1):
    for j in range(0, N-8+1):
        diff = cnt_diff_mat([data[k][j:j+8] for k in range(i, i + 8)])
        result = min(diff, result)
print(result)


#  MxN 배열에서 내부 값으로 mxn 배열을 만드는 list comprehension
#  [sample[i][j:j+3] for j in range(0, 8) for i in range(0, 3)]