class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        # 哈希映射
        inter = {}
        res = []
        for i in nums1:
            if i not in inter:
                inter[i] = 1
            else:
                inter[i] += 1
        for j in nums2:
            if j in inter and inter[j] > 0:
                res.append(j)
                inter[j] -= 1
        return res

    def intersect2(self, nums1: [int], nums2: [int]) -> [int]:
        # 排序+双指针
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        first = second = 0
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        res = []
        while first < nums1_length and second < nums2_length:
            if nums1[first] == nums2[second]:
                res.append(nums1[first])
                first += 1
                second += 1
            elif nums1[first] > nums2[second]:
                second += 1
            else:
                first += 1
        return res


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    s = Solution()
    print(s.intersect2(nums1, nums2))
