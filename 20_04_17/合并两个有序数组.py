class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        双指针法，从后向前遍历
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        # 将nums2剩余元素，排在num1前面
        nums1[:p2 + 1] = nums2[: p2 + 1]


if __name__ == '__main__':
    s = Solution()
    num1 = [1, 2, 0, 0, 0, 0]
    num2 = [2, 5, 6]
    s.merge(num1, 2, num2, 3)
    print(num1)
