def quicksort(arr, low, high):
    if low < high:
        # Partition the array into two subarrays and get the index of the pivot element.
        pivot_index = partition(arr, low, high)

        # Recursively sort the subarrays.
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  # Choose the first element as the pivot.
    l = low + 1
    r = high

    done = False
    while not done:
        while l <= r and arr[l] <= pivot:
            l += 1
        while arr[r] >= pivot and r >= l:
            r -= 1
        if r < l:
            done = True
        else:
            arr[l], arr[r] = arr[r], arr[l]

    # Swap the pivot element with the right element.
    arr[low], arr[r] = arr[r], arr[low]

    return r



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