def linear_search(array, item):
    for index, element in enumerate(array):
        if element == item:
            return index
    return -1


def binary_search(array, item):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_item = array[mid]
        if mid_item == item:
            return mid
        if mid_item < item:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(array, item, left, right):
    mid = left + (right - left) // 2
    mid_item = array[mid]
    if right < left:
        return -1
    if mid_item == item:
        return mid
    if mid_item < item:
        left = mid + 1
    else:
        right = mid - 1
    return binary_search_recursive(array, item, left, right)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item = 7
    index = binary_search_recursive(array, item, 0, len(array) - 1)
    print(f"Index: {index}")
