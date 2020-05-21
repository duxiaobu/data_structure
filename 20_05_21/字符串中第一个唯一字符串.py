class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 哈希法，遍历两次s
        if s:
            res = {}
            for i in s:
                if i not in res:
                    res[i] = 1
                else:
                    res[i] += 1
            for index, item in enumerate(s):
                if res[item] == 1:
                    return index
        return -1


if __name__ == '__main__':
    data = "dddccdbba"
    s = Solution()
    print(s.firstUniqChar(data))