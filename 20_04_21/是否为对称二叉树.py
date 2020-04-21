# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return check(p.left, q.right) and check(p.right, q.left)
        if not root:
            return True
        return check(root.left, root.right)

    def isSymmetric_eg(self, root: TreeNode) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        node_list = [(root.left, root.right)]
        while node_list:
            l, r = node_list.pop(0)
            if not check(l, r):
                return False
            if l:
                node_list.append((l.left, r.right))
                node_list.append((l.right, r.left))
        return True

