class Array:
    """
    使用list实现数组
    """

    def __init__(self, size=32):
        self.size = size
        self.items = [None] * size

    def __getitem__(self, item):
        return self.items[item]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __len__(self):
        return self.size

    def clear(self, value=None):
        for i in range(self.size):
            self.items[i] = value

    def __iter__(self):
        for i in self.items:
            yield i


class MaxHeap:
    """
    最大堆
    """

    def __init__(self, maxSize=None):
        # 保存堆空间初始化大小
        self.maxSize = maxSize
        # 数组保存堆元素
        self._items = Array(maxSize)
        # 堆大小
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        # 判断是否超过堆的空间大小
        if self._count >= self.maxSize:
            raise Exception("maxheap full")
        self._items[self._count] = value
        # 更新数组索引
        self._count += 1
        self._sift_up(self._count - 1)

    def _sift_up(self, index):
        # 维持最大堆特性
        if index > 0:
            # 找到父节点
            parent = (index - 1) // 2
            # 比较插入值和父节点大小
            if self._items[index] > self._items[parent]:
                # 如果大，则交换位置
                self._items[index], self._items[parent] = self._items[parent], self._items[index]
                # 继续递归交换
                self._sift_up(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception("maxheap empty")
        # 保存最大值，即根节点
        value = self._items[0]
        self._count -= 1
        # 将最后一个值赋值到根节点
        self._items[0] = self._items[self._count]
        self._items[self._count] = None
        # 维持堆特性
        self._sift_down(0)
        return value

    def _sift_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        # 只有左孩子
        if left < self._count <= right and self._items[left] > self._items[largest]:
            largest = left
        # 如果左、右孩子都存在
        elif left < self._count and right < self._count and self._items[left] > self._items[largest] and self._items[
            left] > self._items[right]:
            largest = left
        elif right < self._count and self._items[right] > self._items[largest]:
            largest = right
        if largest != index:
            self._items[largest], self._items[index] = self._items[index], self._items[largest]
            self._sift_down(largest)


class MinHeap:
    """
    最小堆
    """

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self._items = Array(maxSize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count > self.maxSize:
            raise Exception("minheap full")
        self._items[self._count] = value
        self._count += 1
        self._sift_up(self._count - 1)

    def _sift_up(self, index):
        if index > 0:
            parent = (index - 1) // 2
            if self._items[index] < self._items[parent]:
                self._items[index], self._items[parent] = self._items[parent], self._items[index]
                self._sift_up(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception("minheap empty")
        value = self._items[0]
        self._count -= 1
        self._items[0] = self._items[self._count]
        self._items[self._count] = None
        self._sift_down(0)
        return value

    def _sift_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        # 既有左子树又有右子树，但是左子树更小
        if left < self._count and \
                right < self._count and \
                self._items[left] < self._items[index] and \
                self._items[left] < self._items[right]:
            self._items[left], self._items[index] = self._items[index], self._items[left]
            self._sift_down(left)
        elif right < self._count and \
                self._items[right] < self._items[index] and \
                self._items[right] < self._items[left]:
            self._items[right], self._items[index] = self._items[index], self._items[right]
            self._sift_down(right)
        # 只有左子树
        elif left < self._count and \
                right >= self._count and \
                self._items[left] < self._items[index]:
            self._items[left], self._items[index] = self._items[index], self._items[left]


import heapq


class TopK:
    """
    求给定列表的前k个最大元素
    """

    def __init__(self, list, k):
        self.min_heap = []
        self.num = k
        self.origin_list = list

    def push(self, value):
        if len(self.min_heap) >= self.num:
            min_value = self.min_heap[0]
            if value < min_value:
                pass
            else:
                heapq.heapreplace(self.min_heap, value)
        else:
            heapq.heappush(self.min_heap, value)

    def get_sort(self):
        for item in self.origin_list:
            self.push(item)
        return self.min_heap


def heap_sort(array):
    # 堆排序问题
    length = len(array)
    max_heap = MaxHeap(length)
    for i in array:
        max_heap.add(i)
    result = []
    for j in range(length):
        result.append(max_heap.extract())
    return result


if __name__ == '__main__':
    # 最大堆测试
    # mHeap = MaxHeap(5)
    # mHeap.add(100)
    # mHeap.add(85)
    # mHeap.add(33)
    # value = mHeap.extract()
    # print(f'value is {value}')
    # for i in mHeap._items:
    #     print(i)

    # 最小堆测试
    # heap = MinHeap(5)
    # heap.add(33)
    # heap.add(85)
    # heap.add(100)
    # value = heap.extract()
    # print(f'value is {value}')
    # for i in heap._items:
    #     print(i)

    a = [3, 5, 2, 9, 6, 4, 7]
    # print(heap_sort(a))
    heap = MaxHeap(10)
    for i in a:
        heap.add(i)
    for j in heap._items:
        print(j)

    # TopK排序问题
    # import random
    # import heapq
    #
    # data = list(range(1000))
    # random.shuffle(data)
    # print(heapq.nlargest(5, data))
    # top = TopK(data, 5)
    # print(top.get_sort())
