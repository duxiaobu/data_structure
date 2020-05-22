class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        strip_str = S.rstrip()
        if len(strip_str) < length:
            diff = length - len(strip_str)
            strip_str += " " * diff
        if len(strip_str) == 0:
            strip_str = " " * length
        str_list = list(strip_str)
        for i in range(len(str_list)):
            if str_list[i] == " ":
                str_list[i] = "%20"
        return "".join(str_list)


if __name__ == '__main__':
    a = '    abc    '
    print(a.rstrip())
    s = Solution()
    print(s.replaceSpaces(a, 2))
