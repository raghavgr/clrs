"""
Merge sort with only the array as input
"""

def mergesort(arr):
    """
    Divide and call merge
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        return merge(left, right)
    return arr

def merge(left, right):
    """
    Combine left and right arrays into sorted a_arr
    """
    a_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a_arr.append(left[i])
            i += 1
        else:
            a_arr.append(right[j])
            j += 1
    a_arr += left[i:]
    a_arr += right[j:]
    return a_arr

A_LIST = [65, 47, 34, 21, 55, 21, 10]
new_a = mergesort(A_LIST)
print(new_a)
