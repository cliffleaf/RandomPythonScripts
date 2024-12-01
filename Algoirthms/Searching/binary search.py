def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

arr = [1, 2, 3, 4, 10, 12]
print(binary_search(arr, 12))
