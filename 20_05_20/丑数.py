class Solution:
    def isUgly(self, num: int) -> bool:
        while num > 1 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
            if num % 2 == 0:
                num = num // 2
            if num % 3 == 0:
                num = num // 3
            if num % 5 == 0:
                num = num // 5
        return num == 1


if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(14))
