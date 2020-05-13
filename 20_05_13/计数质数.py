class Solution:
    def countPrimes(self, n: int) -> int:
        # 暴力破解法
        count = 0
        for i in range(2, n):
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                count += 1
        return count

    def countPrimes2(self, n: int) -> int:
        # 以空间换时间，将基础质数的倍数保存起来
        total = [1] * n
        res = 0
        for i in range(2, n):
            if total[i] == 1:
                res += 1
            j = i
            while i * j < n:
                total[i * j] = 0
                j += 1
        return res

    def countPrimes3(self, n: int) -> int:
        # 还是以空间换时间，只是遍历根号n的前面元素就行
        if n < 2:
            return 0
        total = [1] * n
        total[0] = total[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if total[i] == 1:
                total[i * i:n:i] = [0] * len(total[i * i:n:i])
        return sum(total)


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes3(16))
    # print(a[4:10:2])
