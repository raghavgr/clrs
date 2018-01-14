def iter_binary_search(arr, value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None

print(iter_binary_search([1, 3, 4, 5, 6, 9], 4))