# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        if nums:
            mid = len(nums) // 2
            root = TreeNode(mid)
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1:])


if __name__ == '__main__':
    node_list = [-10, -3, 0, 5, 9]
    print(node_list[:1])
