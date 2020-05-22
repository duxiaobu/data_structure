class Solution:
    def isUnique(self, astr: str) -> bool:
        # 集合运算
        s_set = set(list(astr))
        return len(s_set) == len(astr)

    def isUnique2(self, astr: str) -> bool:
        # 位运算
        # 用来记录出现过的字符
        mask = 0
        for i in astr:
            # 计算偏移量
            offset = ord(i) - ord('a')
            # 偏移offset位后和mask与运算，结果为1则表示已出现过
            if mask & (1 << offset) != 0:
                return False
            else:
                # 否则，将mask该位置1
                mask |= (1 << offset)
        return True


if __name__ == '__main__':
    print()
