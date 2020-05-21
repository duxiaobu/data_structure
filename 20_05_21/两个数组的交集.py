class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        # 工程代码
        set1 = set(nums1)
        set2 = set(nums2)
        inter = set1.intersection(set2)
        return list(inter)

    def intersection2(self, nums1: [int], nums2: [int]) -> [int]:
        inter = set()
        res = []
        for i in nums1:
            if i not in inter:
                inter.add(i)
        for j in nums2:
            if j in inter and j not in res:
                res.append(j)
        return res


if __name__ == '__main__':
    num1 = [1, 2, 2, 1]
    num2 = [2, 2]
    s = Solution()
    print(s.intersection2(num1, num2))
