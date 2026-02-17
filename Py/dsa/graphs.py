from typing import List
import random



random.seed(42)

class BinarySearchTreeNode:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val

    def __repr__(self):
        return str(self.val)

    def insert_node(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert_node(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert_node(val)

    @staticmethod
    def insert_nodes(vals: list, root):
        for i in vals:
            root.insert_node(i)

class BinaryTreeNode:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val

class TreeNode:
    def __init__(self, val:int = "X", children: list =None):
        self.val = val
        self.children = [] if children is None else children

def create_tree(root: TreeNode, depth: int, num_children: int):
    if depth == 0:
        root.val = random.randint(-10,10)
        return root
    for _ in range(num_children):
        child = TreeNode()
        root.children.append(create_tree(child, depth-1, num_children))
    return root

def print_tree(node, prefix="", is_last=True):
    connector = "└── " if is_last else "├── "
    print(prefix + connector + str(node.val))
    prefix += "    " if is_last else "│   "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        print_tree(child, prefix, i == child_count - 1)