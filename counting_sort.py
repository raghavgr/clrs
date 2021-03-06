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
    update the value of count
    whenever its' index == a value in array
    for j = 1 to A.length
        C[A[j]] = C[A[j]] + 1
    update count array with cumulative sum till that index
    for i = 1 to k
        C[i] += C[i - 1]
    Then update result array with results from count array 
    """
    count = [0] * (k + 1)
    for i in arr:
        count[i] = count[i] + 1
    for j in range(1,len(count)):
        count[j] += count[j - 1]
    print(count)
    k = len(arr) - 1
    while k >= 0:
        print(arr[k])
        res[count[arr[k]] - 1] = arr[k]
        print(res)
        count[arr[k]] -= 1
        print(count)
        k -=1


test_arr = [2, 5, 3, 0, 2, 3, 0, 3]
result = [-1]*(len(test_arr))
print(len(test_arr))
counting_sort(test_arr,result )
print(result)