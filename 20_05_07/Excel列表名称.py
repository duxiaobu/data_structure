class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n > 0:
            n, y = divmod(n, 26)
            if y == 0:
                n -= 1
                y = 26
            result = chr(y + 64) + result
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(52))
