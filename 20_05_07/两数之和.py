class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        # 利用字典来存储
        # 时间、空间复杂度O(n)
        data = {}
        for i in range(len(numbers) - 1, -1, -1):
            if target - numbers[i] not in data:
                data[numbers[i]] = i + 1
            else:
                return i + 1, data[target - numbers[i]]

    def twoSum2(self, numbers: [int], target: int) -> [int]:
        # 双指针法
        # 时间复杂度O(n)，空间复杂度O(1)
        # 数组头部
        i = 0
        # 数组尾部
        j = len(numbers) - 1
        while i < j:
            tmp = numbers[i] + numbers[j]
            if tmp == target:
                return [i + 1, j + 1]
            elif tmp > target:
                j = j - 1
            else:
                i = i + 1


if __name__ == '__main__':
    # s = Solution()
    # numbers = [1, 2, 3, 7, 11, 25]
    # target = 9
    # result = s.twoSum2(numbers, target)
    # print(result)
    print(chr(65))
