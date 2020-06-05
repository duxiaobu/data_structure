class Solution:
    def reverseBits(self, num: int) -> int:
        # 记录上个连续1的长度
        pre = 0
        # 记录当前连续1的长度
        cur = 0
        # 在一个转化的情况下，连续1的长度
        res = 1
        bit_length = len(bin(num)) - 2
        for i in range()



if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(117))
    print(len(bin(117)))