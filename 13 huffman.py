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
    for node in c_list:
        heapq.heappush(heap, node(node[1], node[0]))
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        left.huff = 0
        right.huff = 1
        parent = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        print(f'{parent.symbol}->{parent.freq}')
        heapq.heappush(heap, parent)
    return heap
heap = huffman(c_list)
def printNodes(node, val=''):
    appendedCode = val + str(node.huff)
    if(node.left):
        printNodes(node.left, appendedCode)
    if(node.right):
        printNodes(node.right, appendedCode)
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {appendedCode}")
        c_sum.append(len(appendedCode)*node.freq)
printNodes(heap[0])
print("Length is ",sum(c_sum))
print("Average length is ",sum(c_sum)/len(c_list))