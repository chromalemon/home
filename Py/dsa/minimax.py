from graphs import TreeNode, create_tree, print_tree

def minimax(node: TreeNode, depth: int, maximiser: bool, alpha: int = -float("inf"), beta: int = float("inf")):
    if depth == 0:
        return node.val
    if maximiser:
        maxEval = -float("inf")
        for child in node.children:
            eval = minimax(child, depth-1, False, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float("inf")
        for child in node.children:
            eval = minimax(child, depth-1, True, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval
    
if __name__ == "__main__":

    depth=2
    num_children=3

    root = TreeNode()

    create_tree(root, depth, num_children)
    print_tree(root)

    print(f"Optimised value is {minimax(root, depth, maximiser=True)}")

'''
An issue I was stuck on for a while was that in trees.py I had set the default value for "children" in class TreeNode to be "[]". 
This caused errors because the program used the exact same empty list every time I would create a new node. 
Essentially, I thought of children=[] as creating a new empty list each time TreeNode() is called, but instead it created emptyList = [] once and reused
emptyList each time, which caused all children to be appended to one large list. 
Changing the default value to None and initialising the empty list inside of the TreeNode constructor fixed this.

'''