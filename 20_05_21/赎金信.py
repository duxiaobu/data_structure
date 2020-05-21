class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 排序+双指针
        r_list = sorted(ransomNote)
        m_list = sorted(magazine)
        r = m = 0
        r_length = len(r_list)
        m_length = len(m_list)
        while r < r_length and m < m_length:
            if r_list[r] == m_list[m]:
                r += 1
                m += 1
            elif r_list[r] > m_list[m]:
                m += 1
            else:
                return False
        return r == r_length

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        # 哈希
        tmp = {}
        for item in magazine:
            if item not in tmp:
                tmp[item] = 1
            else:
                tmp[item] += 1
        for r in ransomNote:
            if r not in tmp:
                return False
            tmp[r] -= 1
            if tmp[r] < 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct2('a', 'ba'))
