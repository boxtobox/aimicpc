#  I2A 3rd edition
def insertion_sort(arr):
    for j in range(1, arr.__len__()):
        key = arr[j]
        i = j - 1
        while i > 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
        print(arr)




a = '2 4 6 8 3'.split()

insertion_sort(a)

