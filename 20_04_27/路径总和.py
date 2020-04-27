# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        node_list = [(root, sum - root.val)]
        while node_list:
            node, num = node_list.pop()
            if node.left is None and node.right is None and num == 0:
                return True
            if node.left:
                node_list.append((node.left, num - node.left.val))
            if node.right:
                node_list.append((node.right, num - node.right.val))
        return False