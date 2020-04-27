# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        tree_nodes = [(root, 1)]
        while tree_nodes:
            node, depth = tree_nodes.pop(0)
            if node.left:
                tree_nodes.append((node.left, depth + 1))
            if node.right:
                tree_nodes.append((node.right, depth + 1))
            if node.left is None and node.right is None:
                return depth
