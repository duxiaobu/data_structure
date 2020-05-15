# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 遍历的方式，分析规律
        # 时间复杂度O(n)，空间复杂度O(1)
        p_val = p.val
        q_val = q.val
        node = root
        # 从根节点开始遍历
        while node:
            if p_val > node.val and q_val > node.val:
                node = node.right
            elif p_val < node.val and p_val < node.val:
                node = node.left
            else:
                return node


if __name__ == '__main__':
    pass
