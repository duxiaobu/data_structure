import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        b = s.translate(s.maketrans("", "", string.punctuation)).replace(" ", "").lower()
        return b == "".join(list(reversed(b)))

    def isPalindrome2(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        return s == s[::-1]


if __name__ == '__main__':
    s = Solution()
    data = "A man, a plan, a canal: Panama"
    data2 = ""
    # data = data.translate(data.maketrans("", "", string.punctuation)).replace(" ", "").lower()
    print(s.isPalindrome2(data))
