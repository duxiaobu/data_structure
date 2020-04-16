class Solution:
    def climbStairs(self, n: int) -> int:
        prev_num, next_num = 0, 1
        while n > 0:
            prev_num, next_num = next_num, prev_num + next_num
            n -= 1
        return next_num


if __name__ == '__main__':
    s = Solution()
    result = s.climbStairs(6)
    print(result)
