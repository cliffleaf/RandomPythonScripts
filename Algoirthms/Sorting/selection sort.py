# this one below moves the smallest number in each iteration to the first index of the current iteration
def selection_sort_front(arr):
    for i in range(len(arr)):
        min = i 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j 
            
        arr[i], arr[min] = arr[min], arr[i]
    
    return arr 

# this one below moves the largest number in each iteration to the last index of the entire array
def selection_sort_back(arr):	
    for i in range(len(arr) - 1, 0, -1):
        max_idx = 0
        # max_idx already at arr[0], so we start comparing from arr[1]
        for j in range(1, i+1):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[max_idx], arr[i] = arr[i], arr[max_idx]

    return arr

array_front = [9, 8, 6, 7, 4, 6]
array_back = array_front[::]

print(selection_sort_front(array_front))
print(selection_sort_back(array_back))