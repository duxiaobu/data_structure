class Solution:
    def maxProfit(self, prices: [int]) -> int:
        max_profit = 0
        for index in range(1, len(prices)):
            if prices[index] > prices[index - 1]:
                max_profit += prices[index] - prices[index - 1]
        return max_profit


if __name__ == '__main__':
    s = Solution()
    data = [1, 7, 2, 4, 6]
    print(s.maxProfit(data))
