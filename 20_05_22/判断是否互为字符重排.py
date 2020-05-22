class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        # 排序后是否相等
        return sorted(s1) == sorted(s2)

    def CheckPermutation2(self, s1: str, s2: str) -> bool:
        # 位运算
        s11 = 0
        s22 = 0
        for i in s1:
            s11 ^= ord(i)
        for j in s2:
            s22 ^= ord(j)
        if s11 == s22 == 0 and s1[0] != s2[0]:
            return False
        return s11 ^ s22 == 0


if __name__ == '__main__':
   s = Solution()
   print(s.CheckPermutation2('aaa', 'bbb'))