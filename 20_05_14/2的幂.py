class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 时间复杂度为O(logN)
        if n == 1:
            return True
        while n > 1:
            n = n / 2
            if n == 1:
                return True
        return False

    def isPowerOfTwo2(self, n: int) -> bool:
        # 时间、空间复杂度都为O(1)
        # 如果n是2的幂次方，那必定n&(n-1)==0
        return n > 0 and n & (n - 1) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo2(8))
