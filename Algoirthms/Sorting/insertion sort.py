# insertion sort, insert a number in a previous index, like swapping a card on the table
# time complexity: O(n^2)
# best to be used when the array is almost sorted


def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j > -1 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key 


arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)