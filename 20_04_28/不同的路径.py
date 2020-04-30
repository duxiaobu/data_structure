class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 目的地坐标数的路径数f(i,j)=上边坐标的路径数f(i-1,j)+左边坐标的路径数f(i,j-1)
        # 生成MxN的数组
        # 时间、空间复杂度都是O(MxN)，但是可以保存每个点的路径，方便查询
        result = [[1] * m] * n
        for i in range(1, n):
            for j in range(1, m):
                # 状态方程
                result[i][j] = result[i-1][j] + result[i][j-1]
        return result[-1][-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        # 时间复杂度O(MxN),空间复杂度O(n)
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]


if __name__ == '__main__':
    s = Solution()
    data = s.uniquePaths2(7, 3)
    print(data)
