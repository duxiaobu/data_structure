class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        # 旋转得到的字串，只需要两个长度一致，s1是s2二倍的字串
        return len(s1) == len(s2) and s1 in s2 * 2


if __name__ == '__main__':
    s = Solution()
    print(s.isFlipedString("waterbottle", "erbottlewat"))
