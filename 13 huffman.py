import heapq
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, node)):
            return False
        return self.freq == other.freq

c_list = [('a', 5), ('b', 9), ('c', 12), ('d', 13), ('e', 16), ('f', 45)]
c_sum = []
def huffman(c_list):
    heap = []
    for i in c_list:
        heapq.heappush(heap, node(i[1], i[0]))
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        left.huff = 0
        right.huff = 1
        new_node = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        print(new_node.symbol)
        heapq.heappush(heap, new_node)
    return heap
heap = huffman(c_list)
def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")
        c_sum.append(len(newVal)*node.freq)
printNodes(heap[0])
print("Length is ",sum(c_sum))
print("Average length is ",sum(c_sum)/len(c_list))