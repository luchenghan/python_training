class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    tmp = root.left
    root.left = root.right
    root.right = tmp

    invertTree(root.left)
    invertTree(root.right)
    return root


if __name__ == "__main__":
    # Test cases for invert binary tree
    def print_tree(node):
        if not node:
            return "None"
        return f"{node.val}({print_tree(node.left)},{print_tree(node.right)})"
    
    root = TreeNode(4)
    root.left = TreeNode(2) 
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    inverted = invertTree(root)
    print(print_tree(inverted))