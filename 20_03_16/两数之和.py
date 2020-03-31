class Solution:
    """
    两数之和，查找两个元素相加等于目标数的索引值
    """

    def twoSum1(self, nums: [int], target: int) -> [int]:
        # 暴力破解，直接循环遍历查询，时间复杂读O(n^2)，if的判断也会遍历一次
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: [int], target: int) -> [int]:
        n = 0
        for i in range(0, len(nums) - 1):
            # 计算器，这样就能少遍历前面的元素
            n += 1
            if (target - nums[i]) in nums[i + 1:]:
                return [i, nums[i+1:].index(target - nums[i]) + n]

    def twoSum3(self, nums: [int], target: int) -> [int]:
        # 利用字典构造hash结构查询，时间复杂度O(n),空间复杂度O(n)
        dct = {}
        for i, n in enumerate(nums):
            if target - n in dct:
                return [dct[target - n], i]
            dct[n] = i


if __name__ == '__main__':
    s = Solution()
    result = s.twoSum3([3, 3], 6)
    print(result)
    # a = [3, 3]
    # print(a.index(3, 1))
