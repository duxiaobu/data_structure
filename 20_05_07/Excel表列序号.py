class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        bit = 1
        for item in s[::-1]:
            result += (ord(item) - 64) * bit
            bit = bit * 26
        return result


if __name__ == '__main__':
    s = Solution()
    data = s.titleToNumber('ZY')
    print(data)
