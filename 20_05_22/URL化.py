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

    def replaceSpaces2(self, S: str, length: int) -> str:
        s_list = list(S)
        for i in range(length):
            if s_list[i] == " ":
                s_list[i] = "%20"
        print(s_list[: length])
        return "".join(s_list[:length])

    def replaceSpaces3(self, S: str, length: int) -> str:
        return S[:length].replace(" ", "%20")


if __name__ == '__main__':
    a = '    abc    '
    s = Solution()
    print(s.replaceSpaces3(a, 8))
