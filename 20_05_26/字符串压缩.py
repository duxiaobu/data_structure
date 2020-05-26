class Solution:
    def compressString(self, S: str) -> str:
        # 循环拼接
        tmp = S[0]
        res = ""
        count = 0
        for s in S:
            if tmp == s:
                count += 1
            else:
                res += tmp + str(count)
                tmp = s
                count = 1
        res += tmp + str(count)
        return res if len(res) < len(S) else S

    def compressString2(self, S: str) -> str:
        # 双指针
        length = len(S)
        res = ""
        i = 0
        while i < length:
            j = i
            while j < length and S[j] == S[i]:
                j += 1
            res += S[i] + str(j - i)
            i = j
        return res if len(res) < len(S) else S


if __name__ == '__main__':
    data = "aabcccccaaa"
    s = Solution()
    print(s.compressString2(data))
