class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        算法：两数相加实际为相加的个数位 + 两数进制位
        两二进制数做与运算就是个数位，两数做异不为零时，向左偏移移动一位则为进位
        这里只能计算正数
        :param a:
        :param b:
        :return:
        '''
        # 判断进位值是否为0，为0，则两数的异或结果就为最终结果
        while b != 0:
            # 异或相当于两数相加
            tmp = a ^ b
            # 计算进位制，两数相与并左移一位
            b = (a & b) << 1
            a = tmp
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.getSum(1, 5))
