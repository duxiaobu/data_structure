class Solution:
    def mySqrt(self, x: int) -> int:
        # 使用二分法来查找
        if x < 2:
            return x

        left, right = 2, x // 2
        while left <= right:
            pirot = left + (right - left) // 2
            num = pirot * pirot
            if num > x:
                right = pirot - 1
            elif num < x:
                left = pirot + 1
            else:
                return pirot
        return right


if __name__ == '__main__':
    s = Solution()
    b = 3
    print(s.mySqrt(8))
