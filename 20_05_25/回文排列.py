class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # 回文排列，里面的奇数字符最多一个
        tmp = {}
        j_count = 0
        for i in s:
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1
        for count in tmp.values():
            if count % 2 == 1:
                j_count += 1
        return j_count <= 1


if __name__ == '__main__':
   s = Solution()
   print(s.canPermutePalindrome("tactcoa"))