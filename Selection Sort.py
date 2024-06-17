def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    arr = [12, 23, 43, 34, 2, 34, 2]
    selection_sort(arr)
    print(arr)
