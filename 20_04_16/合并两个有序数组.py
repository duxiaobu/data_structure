class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m):
            if nums1[i] > nums2[i]:
                nums1.insert(i, nums2)

