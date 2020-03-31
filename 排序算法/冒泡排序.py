class Bubble(object):
    # 冒泡排序
    # 时间复杂度：最好O(n)，最坏O(n^2),平均O(n^2)
    # 空间复杂度：O(1)
    # 稳定性：稳定
    @staticmethod
    def sort(collection):
        # 基础冒泡排序
        length = len(collection)
        for i in range(length - 1):
            for j in range(length - 1 - i):
                if collection[j] > collection[j + 1]:
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
        return collection

    @staticmethod
    def sort2(collection):
        # 增加跳出判断，如果没有元素交换，就跳出循环
        length = len(collection)
        for i in range(length - 1):
            swapped = False
            for j in range(length - 1 - i):
                if collection[j] > collection[j + 1]:
                    swapped = True
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
            if not swapped:
                break
        return collection

    @staticmethod
    def sort3(collection):
        # 寻找有序和无序元素的临界索引值，这样就只需排序无序元素
        # 根据规律可得，最后一个被交换的元素的索引值就是临界值
        length = len(collection)
        border = length - 1
        for i in range(length - 1):
            swapped = False
            for j in range(border):
                if collection[j] > collection[j + 1]:
                    swapped = True
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
                    border = j
            if not swapped:
                break
        return collection


if __name__ == '__main__':
    data = [3, 2, 5, 8, 4, 9, 6]
    data2 = [3, 4, 2, 1, 5, 6, 7, 8]
    print(Bubble.sort3(data))
