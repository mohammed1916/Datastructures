def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def parent(i):
    return i//2

def max_heapify(a, heap_size, i):
    l = left(i)
    r = right(i)

    largest = i 

    if l < heap_size and a[l] > a[i]:
        largest = l
    
    if r < heap_size and a[r] > a[largest]:
        largest = r 
    
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)
def min_heapify(a, heap_size, i):
    l = left(i)
    r = right(i)

    smallest = i 

    if l < heap_size and a[l] < a[i]:
        smallest = l
    
    if r < heap_size and a[r] < a[smallest]:
        smallest = r 
    
    if smallest != i:
        a[i], a[smallest] = a[smallest], a[i]
        min_heapify(a, heap_size, smallest)


def build_max_heap(a):
    heap_size = len(a)

    for i in range(heap_size//2, 0, -1):
        max_heapify(a, heap_size, i)

def build_min_heap(a):
    heap_size = len(a)

    for i in range(heap_size//2, 0, -1):
        min_heapify(a, heap_size, i)

def main():
    a = [None, 0, 5, 20, 6, 12, 65, 1, 4, 9, 3, 89, 22, 25, 28, 10]
    print(f'Tree: {a[1:]}')
    build_max_heap(a)

    # print heap starting with the root at index 1
    print(f'Heap: {a[1:]}')
    build_min_heap(a)

    # print heap starting with the root at index 1
    print(f'Heap: {a[1:]}')


main()


