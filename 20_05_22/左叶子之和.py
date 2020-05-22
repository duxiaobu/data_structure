# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        total = 0
        if root:
            node_list = [root]
            while node_list:
                node = node_list.pop()
                if node.left and not node.left.left and not node.left.right:
                    total += node.left.val
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
        return total


if __name__ == '__main__':
    pass
