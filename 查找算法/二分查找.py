def binary_search(arr, value):
    # 二分查找就是在一个排好序的列表中查找元素，以中间元素查找
    begin = 0
    end = len(arr) - 1
    while begin < end:
        mid = (begin + end) // 2
        if arr[mid] == value:
            return mid
        if arr[mid] > value:
            end = mid - 1
        else:
            begin = mid + 1
    return -1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(binary_search(a, 4))