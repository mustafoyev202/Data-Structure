def BubbleSort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


if __name__ == '__main__':
    array = [5, 4, 3, 2, 1]
    BubbleSort(array)
    print(array)
