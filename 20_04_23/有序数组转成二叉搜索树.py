# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        # 始终以中间左边为根节点
        def help(left, right):
            if left > right:
                return None
            # 选举根节点
            p = (left + right) // 2
            root = TreeNode(nums[p])
            root.left = help(left, p - 1)
            root.right = help(p + 1, right)
            return root

        return help(0, len(nums) - 1)
