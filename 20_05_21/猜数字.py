# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # 二分查找
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            if res == 1:
                right = mid - 1
            elif res == -1:
                left = mid + 1
            else:
                return mid
