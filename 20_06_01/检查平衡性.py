# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        判定一个二叉树是否平衡：
            1.空树
            2.左右子树都是平衡二叉树
            3.左右子树高度差小于等于1
        """
        # 条件1
        if not root:
            return True

        # 条件2
        left = self.getDepthDFS(root.left)
        right = self.getDepthDFS(root.right)
        if abs(left - right) > 1:
            return False

        # 条件3
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepthDFS(self, root: TreeNode) -> int:
        """
        获取树的最大高度，递归方式
        """
        if not root:
            return 0

        left = self.getDepthDFS(root.left)
        right = self.getDepthDFS(root.right)
        return max(left, right) + 1

    def getDepthBFS(self, root: TreeNode) -> int:
        """
        获取树的最大深度，遍历方式
        """
        # 记录最大深度
        depth = 0
        if root:
            # 节点列表，每个节点保存高度
            node_list = [(root, 1)]
            while node_list:
                node, cur_depth = node_list.pop()
                if node:
                    depth = max(depth, cur_depth)
                    node_list.append((node.left, cur_depth+1))
                    node_list.append((node.right, cur_depth+1))
        return depth
