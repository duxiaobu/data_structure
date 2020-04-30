class Solution:
    def singleNumber(self, nums: [int]) -> int:
        # 时间复杂度O(n)，并且不适用额外的空间
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == '__main__':
    data = [2, 3, 3, 2, 1]
    s = Solution()
    print(s.singleNumber(data))