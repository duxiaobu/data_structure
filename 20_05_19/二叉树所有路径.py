# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> [str]:
        # 迭代
        if not root:
            return []
        node_list = [(root, str(root.val))]
        res = []
        while node_list:
            node, cur_path = node_list.pop()
            if not node.left and not node.right:
                res.append(cur_path)
            if node.left:
                node_list.append((node.left, f'{cur_path}->{node.left.val}'))
            if node.right:
                node_list.append((node.right, f'{cur_path}->{node.right.val}'))
        return res

    def binaryTreePaths2(self, root: TreeNode) -> [str]:
        # 递归
        def get_paths(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    res.append(path)
                else:
                    path += '->'
                    get_paths(node.left, path)
                    get_paths(node.right, path)

        res = []
        get_paths(root, "")
        return res


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.right = node5
    s = Solution()
    print(s.binaryTreePaths2(node1))