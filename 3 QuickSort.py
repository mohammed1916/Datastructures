def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
 
def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)
 



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