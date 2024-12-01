def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


array = [9, 7, 8, 1, 4, 3]

bubble_sort(array)
print(array)