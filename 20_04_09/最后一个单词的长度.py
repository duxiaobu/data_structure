class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        工程代码
        :param s:
        :return:
        """
        return len(s.strip().split(" ")[-1])

    def lengthOfLastWord2(self, s: str) -> int:
        """
        从后向前遍历，先去掉空格，再遍历单词长度
        :param s:
        :return:
        """
        end = len(s) - 1
        while end >= 0 and s[end] == ' ':
            end -= 1
        if end < 0:
            return 0
        start = end
        while start >= 0 and s[start] != ' ':
            start -= 1
        return end - start


if __name__ == '__main__':
    a = 'a bb '
    s = Solution()
    print(s.lengthOfLastWord2(a))
