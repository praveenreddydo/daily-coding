"""This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.

"""



class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

    def insertNode(self, val):
        if self.val is None:
            self.val = val
        elif val<=self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insertNode(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insertNode(val)

    def preOrderTraversal(self):
        A = []
        if self is not None:
            A.append(self.val)
            if self.left is not None:
                A.extend(self.left.preOrderTraversal())
            if self.right is not None:
                A.extend(self.right.preOrderTraversal())
        return A

    def secondHighestElement(self):
        A = self.preOrderTraversal()
        if len(A)<=2:
            return min(A)
        h1, h2 = A[0], A[1]
        for i in range(2, len(A)):
            if A[i]>h1 and A[i]>h2:
                h1, h2 = A[i], h1
            elif A[i]>h2:
                h2 = A[i]
            else:
                pass
        return h2

if __name__=='__main__':
    import random
    myTree = TreeNode()
    for _ in range(10):
        val = random.randint(1, 100)
        myTree.insertNode(val)
    print('Keys =', myTree.preOrderTraversal(), '2nd Highest Element =', myTree.secondHighestElement())
    
    
    
    
    
"""
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.key = data
		self.left = None
		self.right = None
		
# A function to find 2nd largest
# element in a given tree.
def secondLargestUtil(root, c):
	
	# Base cases, the second condition
	# is important to avoid unnecessary
	# recursive calls
	if root == None or c[0] >= 2:
		return

	# Follow reverse inorder traversal so that
	# the largest element is visited first
	secondLargestUtil(root.right, c)

	# Increment count of visited nodes
	c[0] += 1

	# If c becomes k now, then this is
	# the 2nd largest
	if c[0] == 2:
		print("2nd largest element is",
							root.key)
		return

	# Recur for left subtree
	secondLargestUtil(root.left, c)

# Function to find 2nd largest element
def secondLargest(root):
	
	# Initialize count of nodes
	# visited as 0
	c = [0]

	# Note that c is passed by reference
	secondLargestUtil(root, c)

# A utility function to insert a new
# node with given key in BST
def insert(node, key):
	
	# If the tree is empty, return a new node
	if node == None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node

# Driver Code
if __name__ == '__main__':
	
	# Let us create following BST
	#		 50
	#	 /	 \
	#	 30	 70
	#	 / \ / \
	# 20 40 60 80
	root = None
	root = insert(root, 50)
	insert(root, 30)
	insert(root, 20)
	insert(root, 40)
	insert(root, 70)
	insert(root, 60)
	insert(root, 80)

	secondLargest(root)

# This code is contributed by PranchalK


"""
    
