class Node(object):
    # 树节点
    def __init__(self, value, lchild=None, rchild=None):
        self.item = value
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        # 添加节点
        node = Node(value)
        if not self.root:
            # 空树，新添加节点为根节点
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
            else:
                node_queue.append(cur.lchild)
                node_queue.append(cur.rchild)

    def pre(self, root):
        # 先序遍历，递归方式
        if not root:
            return
        print(root.item)
        self.pre(root.lchild)
        self.pre(root.rchild)

    def pre_eg(self, root):
        # 先序遍历，循环方式
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
        # 中序遍历，递归方式
        if not root:
            return
        self.mid(root.lchild)
        print(root.item)
        self.mid(root.rchild)

    def mid_eg(self, root):
        # 中序遍历，递归方式
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
        # 后序遍历，递归方式
        if not root:
            return
        self.beh(root.lchild)
        self.beh(root.rchild)
        print(root.item)

    def beh_eg(self, root):
        # 后序遍历，循环方式
        # 可以先中、右、左遍历，再倒序输出，就是后序的结果
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

    def seq(self, root):
        # 层序遍历，利用队列实现，先进先出
        node_queue = [root]
        out_list = []
        while node_queue:
            node = node_queue.pop(0)
            out_list.append(node.item)
            if node.lchild:
                node_queue.append(node.lchild)
            if node.rchild:
                node_queue.append(node.rchild)
        return out_list

    def max_depth(self, root):
        # 树的最大深度, 利用递归的方式
        if not root:
            return 0
        left = self.max_depth(root.lchild)
        right = self.max_depth(root.rchild)
        return max(left, right) + 1

    def max_depth_eg(self, root):
        # 树的最大深度，利用遍历的方式
        depth = 0
        # 记录节点和层数
        node_queue = []
        if root:
            node_queue.append((root, 1))
        while node_queue:
            node, cur_depth = node_queue.pop()
            if node:
                depth = max(depth, cur_depth)
                node_queue.append((node.lchild, cur_depth + 1))
                node_queue.append((node.rchild, cur_depth + 1))
        return depth

    def min_depth_dfs(self, root):
        # 树的最小深度，采用dfs递归的方式来实现
        if not root:
            return 0
        if not root.lchild:
            return self.min_depth_dfs(root.rchild) + 1
        if not root.rchild:
            return self.min_depth_dfs(root.lchild) + 1
        return min(self.min_depth_dfs(root.lchild), self.min_depth_dfs(root.rchild)) + 1

    def min_depth_bfs(self, root):
        # 树的最小深度，采用bsf方式和队列的数据结构来实现
        if not root:
            return 0
        node_queue = [(root, 1)]
        while node_queue:
            node, depth = node_queue.pop(0)
            if node.lchild:
                node_queue.append((node.lchild, depth + 1))
            if node.rchild:
                node_queue.append((node.rchild, depth + 1))
            if node.lchild is None and node.rchild is None:
                return depth

    def node_count_bfs(self, root):
        # 树的节点数,这里采用广度优先遍历
        if not root:
            return 0
        count = 1
        node_queue = [root]
        while node_queue:
            node = node_queue.pop(0)
            if node.lchild:
                count += 1
                node_queue.append(node.lchild)
            if node.rchild:
                count += 1
                node_queue.append(node.rchild)
        return count

    def node_count_dfs(self, root):
        if not root:
            return 0
        left = self.node_count_dfs(root.lchild)
        right = self.node_count_dfs(root.rchild)
        return left + right + 1

    def leaf_count_bfs(self, root):
        # 获取树的叶子节点，广度优先遍历
        count = 0
        node_queue = []
        if root:
            node_queue.append(root)
        while node_queue:
            node = node_queue.pop(0)
            if node.lchild:
                node_queue.append(node.lchild)
            if node.rchild:
                node_queue.append(node.rchild)
            if not node.lchild and not node.rchild:
                count += 1
        return count

    def leaf_count_dfs(self, root):
        # 获取树的叶子节点，递归方式
        if not root:
            return 0
        if root.lchild is None and root.rchild is None:
            return 1
        return self.leaf_count_dfs(root.lchild) + self.leaf_count_dfs(root.rchild)

    def num_of_k_level_dfs(self, root, k):
        # 获取第K层的节点数
        # 如果根不存在，或者k小于1，则返回0
        if not root or k < 1:
            return 0
        # 如果k等于1，则返回1
        if k == 1:
            return 1
        # 如果k大于1，则返回左子树的k-1层节点和右子树的k-1层级节点
        left = self.num_of_k_level_dfs(root.lchild, k - 1)
        right = self.num_of_k_level_dfs(root.rchild, k - 1)
        return left + right

    def num_of_k_level_bfs(self, root, k):
        # 第k层的节点数，通过k值来循环，队列来存储节点，直到遍历到k-1层时，队列剩下的就是第k层的节点数了
        # num用来记录k-1层有多少个节点，循环num次弹出那些节点。
        if not root or k < 1:
            return 0
        if k == 1:
            return 1
        node_queue = [root]
        num = 1
        curLevelNum = 0
        while k > 1:
            while num > 0:
                node = node_queue.pop(0)
                if node.lchild:
                    node_queue.append(node.lchild)
                    curLevelNum += 1
                if node.rchild:
                    node_queue.append(node.rchild)
                    curLevelNum += 1
                num -= 1
            num = curLevelNum
            k -= 1
        return len(node_queue)

    def is_balance_tree(self, root):
        # 判断二叉树是否是平衡二叉树
        # 平衡二叉树的定义：
        #   1.空树
        #   2.左右子树高度差不大于1
        #   3.左右子树都是平衡二叉树
        # 论证1
        if root is None:
            return True
        ldepth = self.max_depth(root.lchild)
        rdepth = self.max_depth(root.rchild)
        # 论证2
        if abs(ldepth - rdepth) > 1:
            return False
        # 论证3
        return self.is_balance_tree(root.lchild) and self.is_balance_tree(root.rchild)

    def is_complete_tree(self, root):
        # 是否完全二叉树
        # 这位博主讲的很透彻https://blog.csdn.net/qq_40938077/article/details/80471997
        if not root:
            return True
        isLeaf = False
        node_queue = [root]
        while node_queue:
            node = node_queue.pop(0)
            # 如果是叶子节点时，但该节点又有左子节点或右子节点就报错，或者左节点无值，右节点有值也报错
            if (isLeaf and (node.lchild is not None or node.rchild is not None)) or (
                    node.lchild is None and node.rchild is not None):
                return False
            if node.lchild:
                node_queue.append(node.lchild)
            if node.rchild:
                node_queue.append(node.rchild)
            # 叶子节点的标志
            if (node.lchild is None and node.rchild is None) or (node.lchild and node.rchild is None):
                isLeaf = True
        return True

    def is_search_tree(self, root):
        # 是否为搜索二叉树，搜索二叉树特点
        # 节点左子树的值小于节点
        # 节点右子树的值大于节点
        # 左右子树也是搜索二叉树
        # 一个节点也是搜索二叉树
        # 中序遍历结果是一个单向递增的序列，遍历比较
        # 待调整
        if not root:
            return True
        node = root
        node_queue = []
        while node or node_queue:
            while node:
                node_queue.append(node)
                node = node.lchild
            node = node_queue.pop()
            if node.rchild.item <= node.item:
                return False
            if node.item <= node.lchild.item:
                return False
            node = node.rchild
        return True

    def is_same_tree(self, root1, root2):
        # 是否为两个一样的二叉树
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        if root1.item != root2.item:
            return False
        left = self.is_same_tree(root1.lchild, root2.lchild)
        right = self.is_same_tree(root1.rchild, root2.rchild)
        return left and right

    def is_mirror(self, root1, root2):
        # 两个二叉树是否互为镜像
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.item != root2.item:
            return False
        return self.is_mirror(root1.lchild, root2.rchild) and self.is_mirror(root1.rchild, root2.lchild)

    def mirror_tree_dfs(self, root):
        # 镜像二叉树，或者反转二叉树，递归的方式实现
        if not root:
            return None
        # 交换左右节点
        root.lchild, root.rchild = root.rchild, root.lchild
        # 递归子节点
        self.mirror_tree_dfs(root.lchild)
        self.mirror_tree_dfs(root.rchild)

    def mirror_tree_bfs(self, root):
        # 镜像二叉树，遍历方式实现
        if not root:
            return
        node_queue = [root]
        while node_queue:
            node = node_queue.pop(0)
            node.lchild, node.rchild = node.rchild, node.lchild
            if node.lchild:
                node_queue.append(node.lchild)
            if node.rchild:
                node_queue.append(node.rchild)

    def insert_bfs(self, root, value):
        # 在二叉树中插入元素，会比较节点大小，和add方法有所区别
        node = Node(value)
        if not root:
            root = node
        node = root
        while node:
            # 插入左子节点
            if value < node.item:
                if node.lchild is None:
                    node.lchild = node
                    break
                node = node.lchild
            # 插入右子节点
            if value > node.item:
                if node.rchild is None:
                    node.rchild = node
                    break
                node = node.rchild
        return root

    def insert_dfs(self, root, value):
        if not root:
            return Node(value)
        if value < root.item:
            root.lchild = self.insert_dfs(root.lchild, value)
        if value > root.item:
            root.rchild = self.insert_dfs(root.rchild, value)
        return root


if __name__ == '__main__':
    tree = Tree()
    arr = [9, 5, 12, 4, 6, 10, 15]
    for i in arr:
        tree.add(i)
    # tree.pre(tree.root)
    # tree.pre_eg(tree.root)
    # tree.mid(tree.root)
    # tree.mid_eg(tree.root)
    # tree.beh_eg(tree.root)
    # print(tree.seq(tree.root))
    # print(tree.max_depth(tree.root))
    # print(tree.max_depth_eg(tree.root))
    # print(tree.min_depth_dfs(tree.root))
    # print(tree.min_depth_bfs(tree.root))
    # print(tree.node_count_bfs(tree.root))
    # print(tree.node_count_dfs(tree.root))
    # print(tree.leaf_count_bfs(tree.root))
    # print(tree.leaf_count_dfs(tree.root))
    # print(tree.num_of_k_level_dfs(tree.root, 3))
    # print(tree.num_of_k_level_bfs(tree.root, 3))
    # print(tree.is_balance_tree(tree.root))
    # tree.pre(tree.root)
    # tree.mirror_tree_bfs(tree.root)
    # tree.pre(tree.root)
    tree.mid(tree.root)
    print(tree.is_search_tree(tree.root))