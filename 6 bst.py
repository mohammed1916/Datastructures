class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")
   
def min(root):
    min_val = root.data
    while root != None:
        min_val = root.left.data
        root = root.left
    return min_val
    
def delete(root,val):
    if root ==None:
        return root
    if root.val > val:
        root.left = delete(root.left, val)
    elif root.val < val:
        root.right = delete(root.right, val)
    elif root.val == val:
        if root.right == None:
            return root.left
        if root.left == None:
            return root.right
        root.val = min(root.right)
        root.right = delete(root.right, root.val)
    return root
  

     

r = Node(3)
insert(r, 2)
insert(r, 1)
insert(r, 5)
insert(r, 4)
insert(r, 6)
delete(r, 2)

print("\nInorder Traversal:")
inorder(r)
print("\n\nPreorder Traversal:")
preorder(r)
print("\n\nPost order Traversal:")
postorder(r)
print("\n")    