import random


def inset_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


if __name__ == '__main__':
    # 时间复杂度：O(n^2)
    # 空间复杂度：O(1)
    # 稳定性：稳定
    a = list(range(20))
    random.shuffle(a)
    print(a)
    print(inset_sort(a))
