# Python3 code to implement the approach

# Class describing a node of tree
class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v

# Inorder Traversal
def printInorder(root):
    if root:
        # Traverse left subtree
        printInorder(root.left)
        
        # Visit node
        print(root.data,end=" ")
        
        # Traverse right subtree
        printInorder(root.right)

# Driver code
if __name__ == "__main__":
    # Build the tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("Inorder Traversal:",end=" ")
    printInorder(root)

    # This code is contributed by ajaymakvana.
