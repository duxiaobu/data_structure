class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]

    def test(self, x: int) -> bool:
        if x < 0:
            return False

        m, n = x, 0

        while m:
            n = n * 10 + m % 10
            m = m // 10

        if x == n:
            return True
        else:
            return False


if __name__ == '__main__':
    x = 1221
    s = Solution()
    print(s.isPalindrome(x))