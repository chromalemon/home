class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorderTraversal(root):
    if root is None:
        return 
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.data, end=" ")

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(6)
    print("Postorder traversal: ", end='')
    postorderTraversal(root)
    print()

if __name__ == "__main__":
    main()
        
        
