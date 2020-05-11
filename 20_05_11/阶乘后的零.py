class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 暴力破解法
        res = 1
        for i in range(1, n + 1):
            res *= i
        count = 0
        ys = res % 10
        res = res / 10
        while ys == 0:
            count += 1
            ys = res % 10
            res = res / 10
        return count

    def trailingZeroes2(self, n: int) -> int:
        # 统计5的个数
        count = 0
        while n >= 5:
            n = n // 5
            count += n
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes2(30))
