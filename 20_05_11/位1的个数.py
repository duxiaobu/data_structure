class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            tmp = n & 1
            if tmp:
                count += 1
            n >>= 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(13))
