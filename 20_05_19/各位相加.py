class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = eval('+'.join(n for n in str(num)))
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(123))
