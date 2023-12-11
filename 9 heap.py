def getLeftIndex(i):
    return 2*i

def getRightIndex(i):
    return 2*i + 1

# def parent(i):
#     return i//2

def max_heapify(a, heap_size, i):
    l = getLeftIndex(i)
    r = getRightIndex(i)

    largest = i 

    if l < heap_size and a[l] > a[i]:
        largest = l
    
    if r < heap_size and a[r] > a[largest]:
        largest = r 
    
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)
def min_heapify(a, heap_size, currentNodeIndex):
    leftChildIndex = getLeftIndex(currentNodeIndex)
    rightChildIndex = getRightIndex(currentNodeIndex)

    indexOfSmallest = currentNodeIndex 

    if leftChildIndex < heap_size and a[leftChildIndex] < a[currentNodeIndex]:
        indexOfSmallest = leftChildIndex
    
    if rightChildIndex < heap_size and a[rightChildIndex] < a[indexOfSmallest]:
        indexOfSmallest = rightChildIndex 
    
    if indexOfSmallest != currentNodeIndex:
        a[currentNodeIndex], a[indexOfSmallest] = a[indexOfSmallest], a[currentNodeIndex]
        min_heapify(a, heap_size, indexOfSmallest)


def build_max_heap(a):
    heap_size = len(a)

    for i in range(heap_size//2, 0, -1):
        max_heapify(a, heap_size, i)

def build_min_heap(a):
    heap_size = len(a)

    for i in range(heap_size//2, 0, -1):
        min_heapify(a, heap_size, i)

def delete_max(a):
    heap_size = len(a)
    if heap_size == 0:
        print('Heap underflow')
    
    a[1] = a[heap_size - 1]
    heap_size -= 1
    a.pop(heap_size-1)
    max_heapify(a, heap_size, 1)

def delete_min(a):
    heap_size = len(a)
    if heap_size == 0:
        print('Heap underflow')
    
    a[1] = a[heap_size - 1]
    a.pop(heap_size-1)
    heap_size -= 1
    min_heapify(a, heap_size, 1)


def main():
    # print heap starting with the root at index 1
    # https://stackoverflow.com/questions/22900388/why-in-a-heap-implemented-by-array-the-index-0-is-left-unused
    #  having the root at 0 rather than at 1 costs you an extra add to find the left child, and an extra subtraction to find the parent.
    print("Initial array: ")
    max_a = [None, 0, 5, 20, 6, 12, 65, 1, 4, 9, 3, 89, 22, 25, 28, 10]
    min_a = [None, 0, 5, 20, 6, 12, 65, 1, 4, 9, 3, 89, 22, 25, 28, 10]
    print(f'Tree: (Max){max_a[1:]}')
    print(f'Tree: (Min){min_a[1:]}')

    # Build heap
    print("Build max heap: ")
    build_max_heap(max_a)
    print(f'Heap: {max_a[1:]}')

    print("Build min heap: ")
    build_min_heap(min_a)
    print(f'Heap: {min_a[1:]}')

    # Heap Delete 
    print("Delete max: ")
    delete_max(max_a)
    print(f'Heap: {max_a[1:]}')

    print("Delete min: ")
    delete_min(min_a)
    print(f'Heap: {min_a[1:]}')


main()


