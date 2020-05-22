class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_point = t_point = 0
        s_length = len(s)
        t_length = len(t)
        while s_point < s_length and t_point < t_length:
            if s[s_point] == t[t_point]:
                s_point += 1
                t_point += 1
            else:
                t_point += 1
        return s_point == s_length


if __name__ == '__main__':
    str1 = "ab"
    str2 = "adfbdc"
    s = Solution()
    print(s.isSubsequence(str1, str2))
