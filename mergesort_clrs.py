"""
Merge sort according to CLRS
"""

def mergesort(arr, left, right):
    """
    The divde part of merge sort.
    """
    if left < right:
        mid = (left + right) // 2
        mergesort(arr, left, mid)
        mergesort(arr, mid+1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    """
    Merges left and right side of array arr
    """
    # lengths of left and right arrays
    left_len = mid - left + 1
    right_len = right - mid
    # temp arrays
    left_arr = [0] * left_len
    right_arr = [0] * right_len
    # fill up the right and left arrays
    for i in range(0, left_len):
        print(left + i)
        left_arr[i] = arr[left + i]
    for i in range(0, right_len):
        right_arr[i] = arr[mid + 1 + i]
    i, j = 0, 0
    k = left
    while i < left_len and j < right_len:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i = i + 1
        else:
            arr[k] = right_arr[j]
            j = j + 1
        k = k + 1
    while i < left_len:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < right_len:
        arr[k] = right_arr[i]
        j += 1
        k += 1
    # arr += left_arr[j:]
    # arr += right_arr[k:]

A_LIST = [65, 47, 34, 21, 55, 21, 10]
mergesort(A_LIST, 0, len(A_LIST) - 1)
print(A_LIST)
