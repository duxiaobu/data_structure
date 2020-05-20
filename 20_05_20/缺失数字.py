class Solution:
    def missingNumber(self, nums: [int]) -> int:
        # 工程代码
        full = set(range(0, len(nums) + 1))
        target = full.difference(nums)
        return target.pop()

    def missingNumber2(self, nums: [int]) -> int:
        # 数学法
        dream_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return dream_sum - actual_sum

    def missingNumber3(self, nums: [int]) -> int:
        # 异或法，同一数字异或为0
        miss = len(nums)
        for i, item in enumerate(nums):
            miss ^= i ^ item
        return miss


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber3([2, 0, 1]))
