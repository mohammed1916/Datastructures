def mergeSort(a):
    if len(a) > 1:

        r = len(a)//2
        L = a[:r]
        M = a[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            a[k] = M[j]
            j += 1
            k += 1


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

a = [10, 7, 8, 9, 1, 5]
print("\nUnsorted list:")
printList(a)

mergeSort(a)
print("\nSorted list:")
printList(a)