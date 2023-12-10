def max_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
        
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)
def min_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)
def deleteMaxRoot(arr):
    lastElement = arr[len(arr) - 1]
    arr[0] = lastElement
    n=len(arr) 
    arr.pop(n-1)
    max_heapify(arr, 0)
def deleteMinRoot(arr):
    lastElement = arr[len(arr) - 1]
    arr[0] = lastElement
    n=len(arr) 
    arr.pop(n-1)
    min_heapify(arr, 0)
def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A,k)
def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A,k)
        
max_A=[]
min_A=[]
n=0
maxval=True
ch=1
while(maxval):
    print("1.Max-Heap\n2.Min-Heap\n3.Exit")
    val=True
    choice=int(input("Enter your choice :"))
    while(val):
        if(choice==1):
            print("1.Insert\n2.Delete\n3.Exit\n")
            ch=int(input("Enter your choice to perform max-heap:: "))
            if(ch==1):
                a=int(input("Enter the value "))
                max_A.append(a)
                build_max_heap(max_A)
                print(max_A)
            if(ch==2):
                deleteMaxRoot(max_A)
                print(max_A)
            if(ch==3):
                val=False
                
        if(choice==2):
            print("1.Insert\n2.Delete\n3.Exit\n")
            ch=int(input("Enter your choice to perform min-heap:: "))
            if(ch==1):
                a=int(input("Enter the value "))
                min_A.append(a)
                build_min_heap(min_A)
                print(min_A)
            if(ch==2):
                deleteMinRoot(min_A)
                print(min_A)
            if(ch==3):
                val=False
                
        if(choice==3):
             maxval=False
             exit(0)
