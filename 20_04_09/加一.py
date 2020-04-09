class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        """
        从最后遍历，等9进位，最后头插入1；不等9，则直接加1
        :param digits:
        :return:
        """
        # 因为倒序遍历，为了能遍历到第一次元素，所以len(xx) + 1
        for i in range(1, len(digits)+1):
            if digits[-i] != 9:
                digits[-i] += 1
                return digits
            digits[-i] = 0
        digits.append(0)
        digits[0] = 1
        return digits


if __name__ == '__main__':
    s = Solution()
    a = [9, 9]
    print(s.plusOne(a))
