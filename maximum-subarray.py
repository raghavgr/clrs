"""
Maximum subarray problem: 
In an array of numbers, find the contiguous subarray of numbers
with the largest sum
"""
def maximum_subarray_bf(arr):
    """ 
    Brute force solution to maximum subarray problem 
    :type arr: List[int]
    :rtype: (int, int, int)
    """
    curr_max = arr[0]
    left = 0
    right = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum >= curr_max:
                curr_max = sum
                left = i
                right = j
    return (left, right, curr_max)

def maximum_subarray(arr, low, high):
    """
    Divide and conquer method of solving maximum subarray problem.
    :type arr: List[int]
    :type low, high: int
    :rtype: (int, int, int)
    """
    if high == low:
        return (low, high, arr[low])
    mid = (low + high) // 2

    left = maximum_subarray(arr, low, mid)
    right = maximum_subarray(arr, mid+1, high)
    cross = maximum_crossing_subarray(arr, low, mid, high)

    if left[2] >= right[2] and left[2] >= cross[2]:
        return left
    elif right[2] >= left[2] and right[2] >= cross[2]:
        return right
    else:
        return cross

def maximum_crossing_subarray(arr, low, mid, high):
    """
    A helper used to find if there is a contiguous subarray with the largest sum 
    of the array such that middle element of the array is part of it.
    :type arr: List[int]
    :type low, mid, high: int
    :rtype: (int, int, int)
    """
    left_sum = -9223372036854775808       # import sys, -sys.maxsize -1, lowest number
    sum = 0
    left_max = 0
    for i in range(mid, low-1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum =sum
            left_max = i
    right_sum = -9223372036854775808
    sum = 0
    right_max = 0
    print(high)
    for i in range(mid + 1, high+1):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
            right_max = i
    return (left_max, right_max, left_sum + right_sum)



A_LIST = [-2,1,-3,4,-1,2,1,-5,4]
b_list = [-2, -5, 6, -2, -3, 1, 5, -6]
print(maximum_subarray(b_list, 0, len(b_list) - 1))
print(maximum_subarray([1, 2], 0, 2 - 1))
