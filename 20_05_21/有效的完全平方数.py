class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 暴力破解法
        i = 1
        while i * i < num:
            i += 1
        return i * i == num

    def isPerfectSquare2(self, num: int) -> bool:
        # 二分查找
        if num < 2:
            return True

        left = 2
        right = num // 2
        while left <= right:
            mid = (left + right) // 2
            mid_res = mid * mid
            if mid_res == num:
                return True
            elif mid_res > num:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPerfectSquare2(81))
