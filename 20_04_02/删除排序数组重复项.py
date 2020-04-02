class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)

    def removeDuplicates2(self, nums: [int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == '__main__':
    s = Solution()
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(s.removeDuplicates(a))
    print(a)
