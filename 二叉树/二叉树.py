class Node(object):
    def __init__(self, item, lchild=None, rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return
        node_queue = [self.root]
        while node_queue:
            cur = node_queue.pop(0)
            if not cur.lchild:
                cur.lchild = node
                return
            elif not cur.rchild:
                cur.rchild = node
                return
            node_queue.append(cur.lchild)
            node_queue.append(cur.rchild)

    def pre(self, root):
        if not root:
            return
        print(root.item)
        self.pre(root.lchild)
        self.pre(root.rchild)

    def pre_eg(self, root):
        if not root:
            return
        node_queue = []
        node = root
        while node_queue or node:
            while node:
                print(node.item)
                node_queue.append(node)
                node = node.lchild
            node = node_queue.pop()
            node = node.rchild

    def mid(self, root):
        if not root:
            return
        self.mid(root.lchild)
        print(root.item)
        self.mid(root.rchild)

    def mid_eg(self, root):
        if not root:
            return
        node_queue = []
        node = root
        while node_queue or node:
            while node:
                node_queue.append(node)
                node = node.lchild
            node = node_queue.pop()
            print(node.item)
            node = node.rchild

    def beh(self, root):
        if not root:
            return
        self.beh(root.lchild)
        self.beh(root.rchild)
        print(root.item)

    def beh_eg(self, root):
        # 遍历方式：中->右->左，再倒序输出
        if not root:
            return
        node_q1 = []
        node_q2 = []
        node = root
        while node_q1 or node:
            while node:
                node_q1.append(node)
                node_q2.append(node)
                node = node.rchild
            node = node_q1.pop()
            node = node.lchild
        while node_q2:
            print(node_q2.pop().item)

    def dx(self, root):
        if not root:
            return
        queue = [self.root]
        out_list = []
        while queue:
            cur = queue.pop(0)
            out_list.append(cur.item)
            if cur.lchild:
                queue.append(cur.lchild)
            if cur.rchild:
                queue.append(cur.rchild)
        return out_list

    def max_depth(self, root):
        if not root:
            return 0
        left = self.max_depth(root.lchild)
        right = self.max_depth(root.rchild)
        return max(left, right) + 1

    def max_depth_eg(self, root):
        # 记录节点和层数的栈
        stack = []
        if root:
            stack.append((root, 1))
        depth = 0
        while stack:
            cur_node, cur_depth = stack.pop()
            if cur_node:
                depth = max(depth, cur_depth)
                stack.append((cur_node.lchild, cur_depth + 1))
                stack.append((cur_node.rchild, cur_depth + 1))
        return depth


if __name__ == '__main__':
    tree = Tree()
    for i in ['A', 'B', 'C', 'D', 'E', 'F']:
        tree.add(i)
    # tree.pre(tree.root)
    # tree.mid(tree.root)
    # tree.beh(tree.root)
    # print(tree.dx(tree.root))
    # tree.pre_eg(tree.root)
    # tree.mid_eg(tree.root)
    # tree.beh_eg(tree.root)
    # print(tree.max_depth(tree.root))
    # print(tree.max_depth_eg(tree.root))