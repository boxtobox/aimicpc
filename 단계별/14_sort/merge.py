def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)


def merge(arr, p, q, r):
    arr_left = arr[p:q+1]
    arr_right = arr[q+1:r+1]
    i = j = 0
    k = p
    while i < q - p + 1 and j < r - q:
        if arr_left[i] <= arr_right[j]:
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
