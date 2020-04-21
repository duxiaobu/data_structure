# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    def maxDepth_eg(self, root: TreeNode) -> int:
        depth = 0
        if root:
            node_list = [(root, 1)]
            while node_list:
                node, cur_depth = node_list.pop(0)
                if node:
                    depth = max(depth, cur_depth)
                    node_list.append((node.left, cur_depth + 1))
                    node_list.append((node.right, cur_depth + 1))

        return depth
