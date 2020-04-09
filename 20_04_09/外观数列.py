class Solution:
    def countAndSay(self, n: int) -> str:
        prev_person = '1'
        for i in range(1, n):
            next_person, num, count = '', prev_person[0], 1
            for j in range(1, len(prev_person)):
                if prev_person[j] == num:
                    count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person

    def countAndSay2(self, n: int) -> str:
        prev_person = '1'
        for i in range(1, n):
            # 固定遍历基础值
            next_person, num, count = '', prev_person[0], 1
            # 遍历前一个字符串的每个值，下一个和上一个相等，则计数+1
            for j in range(1, len(prev_person)):
                if prev_person[j] == num:
                    count += 1
                else:
                    # 统计部分值，并初始化num变量和计数count
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay2(6))
