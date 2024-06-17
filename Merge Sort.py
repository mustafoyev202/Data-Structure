# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     return merge_two_sorted_array(left, right)
#
#
# def merge_two_sorted_array(a, b):
#     sorted_list = []
#     len_a = len(a)
#     len_b = len(b)
#     i = j = 0
#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             sorted_list.append(a[i])
#             i += 1
#         else:
#             sorted_list.append(b[j])
#             j += 1
#     while i < len_a:
#         sorted_list.append(a[i])
#         i += 1
#     while j < len_b:
#         sorted_list.append(b[j])
#         j += 1
#     return sorted_list
#
#
# if __name__ == '__main__':
#     arr = [123, 675876, 342, 2, 345]
#     print(merge_sort(arr))


# Second approach
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_array(left, right, arr)


def merge_two_sorted_array(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
            k += 1
        else:
            arr[k] = b[j]
            j += 1
            k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    arr = [123, 675876, 342, 2, 345]
    merge_sort(arr)
    print(arr)
