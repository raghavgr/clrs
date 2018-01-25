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

A_LIST = [-2,1,-3,4,-1,2,1,-5,4]
arr2 = [2, 3, 4, 5, 7]
b_list = [-2, -5, 6, -2, -3, 1, 5, -6]
print(maximum_subarray_bf(A_LIST))
print(maximum_subarray_bf(arr2))
print(maximum_subarray_bf(b_list))