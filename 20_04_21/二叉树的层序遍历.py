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
            node_list = [[root]]
            while node_list:
                node_array = node_list.pop(0)
                result.append([x.val for x in node_array])
                if node_array:
                    tmp = []
                    for node in node_array:
                        tmp.extend([node.left, node.right])
                    node_list.append(filter(None, tmp))
        result.reverse()
        return result


if __name__ == '__main__':
    a = [[3], [2], [1]]
    a.reverse()
    print(a)