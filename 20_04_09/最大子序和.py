class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        n = len(nums)
        # 记录最大值和当前序列和最大值
        end_max = cur_max = nums[0]
        for i in range(1, n):
            cur_max = max(nums[i], cur_max + nums[i])
            end_max = max(end_max, cur_max)
        return end_max


if __name__ == '__main__':
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print(s.maxSubArray(a))
