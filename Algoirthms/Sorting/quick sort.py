# quick sort using 3-way-partitioning, aka the Dutch flag partitioning
# dividing the list into 3 groups, those smaller, equal to and larger than the pivot

# This is classical implementation of divide and conquer model
# Best-case time complexity: O(n logn)
# Average time complexity: O(n logn)
# Worst-case time complexity: O(n^2)

def partition3(arr, left, right):

    pivot = arr[right]
    i = left 
    k = left 

    for j in range(left, right+1):
        if arr[j] == pivot:
            arr[k], arr[j] = arr[j], arr[k]
            k += 1
        if arr[j] < pivot:
            arr[k], arr[j] = arr[j], arr[k]
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
            i += 1
    
    return i-1, k

def quick_sort(arr, low, high):
    if low >= high:
        return 
    
    m, p = partition3(arr, low, high)

    quick_sort(arr, low, m)
    quick_sort(arr, p, high)


# a_list = [9, 8, 7, 6, 5]
a_list = [93, 78, 19, 117, 86, 109, 116, 61]
quick_sort(a_list, 0, len(a_list)-1)

print(a_list)