class Solution:
    def maxProfit(self, prices: [int]) -> int:
        # 默认最大利润为0
        maxprofit = 0
        if prices:
            # 默认第一个为最低价格
            minprice = prices[0]
            # 遍历比较
            for price in prices:
                maxprofit = max(price - minprice, maxprofit)
                minprice = min(price, minprice)
        return maxprofit


if __name__ == '__main__':
    data = [7, 1, 5, 3, 7, 4]
    data2 = [7, 6, 5, 4]
    s = Solution()
    print(s.maxProfit([]))