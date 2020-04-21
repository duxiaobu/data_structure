# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        # 添加节点
        node = TreeNode(value)
        if not self.root:
            # 空树，新添加节点为根节点
            self.root = node
            return
        node_queue = [self.root]
        while node_queue:
            cur = node_queue.pop(0)
            if not cur.left:
                cur.left = node
                return
            elif not cur.right:
                cur.right = node
                return
            else:
                node_queue.append(cur.left)
                node_queue.append(cur.right)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree_eg(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        node_list = [(p, q)]
        while node_list:
            p, q = node_list.pop(0)
            if not check(p, q):
                return False
            if p:
                node_list.append((p.left, q.left))
                node_list.append((p.right, q.right))
        return True

if __name__ == '__main__':
    s = Solution()
    p = Tree()
    p.add(1)
    p.add(2)
    q = Tree()
    q.add(1)
    # q.add(None)
    q.add(2)
    print(s.isSameTree(p.root, q.root))
