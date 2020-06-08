from sys import stdin


def insertion_sort(arr):
    for j in range(1, arr.__len__()):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key


N = int(stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(stdin.readline()))
insertion_sort(arr)
print(*arr, sep='\n')
