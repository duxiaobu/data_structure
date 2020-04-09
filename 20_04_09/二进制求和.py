class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 将二进制转化为10进制相加，结果输出为二进制
        return '{0:b}'.format(int(a, 2) + int(b, 2))

    def addBinary2(self, a: str, b: str) -> str:
        """
        用0将a,b补全为一样长，相同位依次判断比较
        :param a:
        :param b:
        :return:
        """
        length = max(len(a), len(b))
        a, b = a.zfill(length), b.zfill(length)
        result = []
        carry = 0
        for i in range(length - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                result.append('1')
            else:
                result.append('0')
            carry //= 2
        if carry == 1:
            result.append('1')
        result.reverse()
        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    result = s.addBinary2('1111', '0110')
    print(result)