def quicksort(arr, low, high):
    if low < high:
        # Partition the array into two subarrays and get the index of the pivot element.
        pivot_index = partition(arr, low, high)

        # Recursively sort the subarrays.
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  # Choose the first element as the pivot.
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # Swap the pivot element with the right element.
    arr[low], arr[right] = arr[right], arr[low]

    return right



def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

a = [10, 7, 8, 9, 1, 5]
print("\nUnsorted list:")
printList(a)
quicksort(a, 0, len(a) - 1)
print("\nSorted list:")
printList(a)