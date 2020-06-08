from sys import stdin


def merge_sort(arr, p, r, key):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q, key)
        merge_sort(arr, q+1, r, key)
        merge(arr, p, q, r, key)


def merge(arr, p, q, r, key):
    arr_left = arr[p:q+1]
    arr_right = arr[q+1:r+1]
    i = j = 0
    k = p
    while i < q - p + 1 and j < r - q:
        if arr_left[i][key] <= arr_right[j][key]:
            arr[k] = arr_left[i]
            i += 1
        else:
            arr[k] = arr_right[j]
            j += 1
        k += 1
    while i < q - p + 1:
        arr[k] = arr_left[i]
        i += 1
        k += 1
    while j < r - q:
        arr[k] = arr_right[j]
        j += 1
        k += 1


N = int(stdin.readline())
users = [(int(a), b) for a, b in [stdin.readline().rstrip().split(' ') for _ in range(N)]]
merge_sort(users, 0, len(users)-1, 0)
for user in users:
    print(user[0], user[1])
