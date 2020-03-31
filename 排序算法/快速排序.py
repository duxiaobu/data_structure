def quick_sort(collection):
    small = []
    equal = []
    big = []
    if len(collection) > 1:
        pivot = collection[0]
        for i in collection:
            if i < pivot:
                small.append(i)
            if i == pivot:
                equal.append(i)
            if i > pivot:
                big.append(i)
        return quick_sort(small) + equal + quick_sort(big)
    return collection


def quick2_sort(data: list, start: int, end: int):
    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = data[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and data[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        data[low] = data[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and data[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        data[high] = data[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    data[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick2_sort(data, start, low - 1)

    # 对基准元素右边的子序列进行快速排序
    quick2_sort(data, low + 1, end)


if __name__ == '__main__':
    # 平均时间复杂度：n*log2n
    # 稳定性：不稳定排序
    a = [3, 9, 2, 5, 1, 2, 6, 4, 7, 3]
    b = [3, 9, 2, 5]
    print(quick_sort(a))
    quick2_sort(a, 0, len(a) -1)
    print(a)