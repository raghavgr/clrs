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

def binary_search(arr, value, low, high):
    mid = (low + high) // 2
    if value == arr[mid]:
        return mid
    elif value > arr[mid]:
        return binary_search(arr, value, mid + 1, high)
    else:
        return binary_search(arr, value, low, mid - 1)

test_arr = [1, 3, 4, 5, 6, 9]
print(iter_binary_search(test_arr, 4))
print(binary_search(test_arr, 4, 0, len(test_arr) ))