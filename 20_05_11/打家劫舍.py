class Solution:
    def rob(self, nums: [int]) -> int:
        """
        动态规划
        1. 找出子问题
        2. 找出子问题推导式
        3. 确定DP数组计算顺序
        4. 优化空间
        """
        if not nums:
            return 0

        length = len(nums)
        # 定义边界值
        dp = [0] * (length + 1)
        dp[1] = nums[0]
        for i in range(2, length + 1):
            # 选举最大值，前一间房子的钱或者当前房子的钱加上前前房子的钱
            dp[i] = max(dp[i - 1], nums[i-1] + dp[i - 2])
        return dp[length]

    def rob2(self, nums: [int]) -> int:
        # 空间复杂度优化，当前值只需要前两个的值
        cur, prev = 0, 0
        for num in nums:
            cur, prev = max(cur, num + prev), cur
        return cur


if __name__ == '__main__':
    data = [2, 1, 1, 2, 1]
    s = Solution()
    print(s.rob2(data))
