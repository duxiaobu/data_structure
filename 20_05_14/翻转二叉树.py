# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 翻转每个子节点，迭代的方式
        if not root:
            return None
        node_list = [root]
        while node_list:
            node = node_list.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                node_list.append(node.left)
            if node.right:
                node_list.append(node.right)
        return root

    def invertTree2(self, root: TreeNode) -> TreeNode:
        # 迭代的方式
        if not root:
            return None
        root.left, root.right = root.right, root.left
        # 迭代左右子树
        self.invertTree2(root.left)
        self.invertTree2(root.right)
        return root


if __name__ == '__main__':
    pass
