def swap(a, b, arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]
    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, arr)
    swap(pivot_index, end, arr)
    return end


def QuickSort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        QuickSort(arr, start, pi - 1)
        QuickSort(arr, pi + 1, end)


if __name__ == '__main__':
    arr = [100, 20, 3087, 405, 5022, 60, 700, 80, 90, 100]
    QuickSort(arr, 0, len(arr) - 1)
    print(arr)
