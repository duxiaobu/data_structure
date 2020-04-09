class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        parent_length = len(haystack)
        child_length = len(needle)
        for i in range(parent_length - child_length + 1):
            if haystack[i:i + child_length] == needle:
                return i
        return -1
