# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        result = []
        if root:
            node_list = [root]
            while node_list:
                tmp = []
                for _ in range(len(node_list)):
                    node = node_list.pop(0)
                    tmp.append(node.val)
                    if node.left:
                        node_list.append(node.left)
                    if node.right:
                        node_list.append(node.right)
                result.append(tmp)
        return result[::-1]


if __name__ == '__main__':
    pass