"""
Implementation of counting sort from CLRS
"""
def counting_sort(arr, res):

    k = max(arr)
    
    """
    create a count array until max of arr (k).
    CLRS code:
    let C[0:k]  be a new array 
    for i=0 to k
        c[i] = 0
    """
    count = [0] * (k + 1)
    """
    for j = 1 to A.length
        C[A[j]] = C[A[j]] + 1
    """
    for i in arr:
        count[i] = count[i] + 1
    for j in range(1,len(count)):
        count[j] += count[j - 1]
    k = len(arr) - 1
    while k >= 0:
        print(arr[k])
        res[count[arr[k]] - 1] = arr[k]
        count[arr[k]] -= 1
        k -=1


test_arr = [1, 12, 6, 0 ,3, 4, 3, 5]
result = [0]*(len(test_arr))
print(len(test_arr))
counting_sort(test_arr,result )
print(result)