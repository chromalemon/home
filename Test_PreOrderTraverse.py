class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to perform preorder traversal
def preorderTraversal(root):
  
    # Base case
    if root is None:
        return
      
    # Visit the current node
    print(root.data, end=' ')
    
    # Recur on the left subtree
    preorderTraversal(root.left)
    
    # Recur on the right subtree
    preorderTraversal(root.right)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(6)
    print("preorder traversal: ", end='')
    preorderTraversal(root)
    print()

if __name__ == "__main__":
    main()
