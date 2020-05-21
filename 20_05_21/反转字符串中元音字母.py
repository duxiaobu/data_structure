class Solution:
    def reverseVowels(self, s: str) -> str:
        # 双指针
        left = 0
        right = len(s) - 1
        s_list = list(s)
        vowels = "aoeiuAOEIU"
        while left < right:
            if s_list[left] in vowels and s_list[right] not in vowels:
                right -= 1
            elif s_list[left] not in vowels and s_list[right] in vowels:
                left += 1
            elif s_list[left] in vowels and s_list[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            else:
                left += 1
                right -= 1
        return ''.join(s_list)


if __name__ == '__main__':
    s = Solution()
    data = "aA"
    print(s.reverseVowels(data))
