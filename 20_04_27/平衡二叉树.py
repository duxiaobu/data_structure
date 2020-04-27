# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 判断一颗二叉树是否为平衡二叉树
        # 1.空树为平衡二叉树
        # 2.左右子树高度差不大于1
        # 3.左右子树都是平衡二叉树
        def max_depth(root):
            if not root:
                return 0
            left = max_depth(root.left)
            right = max_depth(root.right)
            return max(left, right) + 1
        if not root:
            return True
        left = max_depth(root.left)
        right = max_depth(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
