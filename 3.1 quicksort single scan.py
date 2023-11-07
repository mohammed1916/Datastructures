def partition(a, f, l):
    p=a[l]
    next = f-1
    for k in range(f,l):
        if a[k] <= p:
            next +=1
            a[k], a[next] = a[next], a[k] 
    a[next+1], a[l] = a[l], a[next+1]
    return next + 1

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

"""

OUTPUT:
Unsorted list:
10 7 8 9 1 5 

Sorted list:
1 5 7 8 9 10
"""