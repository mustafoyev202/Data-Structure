def ShellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap //= 2


if __name__ == '__main__':
    arr = [12, 3, 4, 2, 1, 23, 23, 41, 2, 4]
    ShellSort(arr)
    print(arr)
