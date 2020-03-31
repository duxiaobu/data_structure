# 线性查找就是每个元素比较，相等即返回数据
def line_find(arr, value):
    for (index, key) in enumerate(arr):
        if key == value:
            return index
    return -1


if __name__ == '__main__':
    print(line_find([3, 5, 7, 2, 4], 2))
