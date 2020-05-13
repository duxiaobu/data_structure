class Solution:
    def isHappy(self, n: int) -> bool:
        # 使用set集合来检测是否有重复项
        # 计算下一个数
        def getNext(n):
            total = 0
            while n > 0:
                n, mod = divmod(n, 10)
                total += mod ** 2
            return total

        # 是否等于1和是否进入循环
        elements = set()
        while n != 1 and n not in elements:
            elements.add(n)
            n = getNext(n)
        return n == 1

    def isHappy2(self, n: int) -> bool:
        # 快慢指针
        def getNext(n):
            sum_total = 0
            while n > 0:
                n, mod = divmod(n, 10)
                sum_total += mod ** 2
            return sum_total

        slow = n
        fast = getNext(n)
        while fast != 1 and slow != fast:
            slow = getNext(n)
            fast = getNext(getNext(fast))
        return fast == 1


if __name__ == '__main__':
    s = Solution()
    res = s.isHappy2(19)
    print(res)
