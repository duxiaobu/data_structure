class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        # 自己的方法
        for item in nums:
            if item == val:
                while item in nums:
                    nums.remove(item)
        return len(nums)

    def removeElement2(self, nums: [int], val: int) -> int:
        # 官方推荐的方法
        # 记录不相等的元素个数，并且用来保存元素索引
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == '__main__':
    a = [1, 3, 1, 2, 5, 2]
    s = Solution()
    print(s.removeElement(a, 3))
