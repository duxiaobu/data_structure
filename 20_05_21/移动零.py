class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


if __name__ == '__main__':
    s = Solution()
    data = [0, 1, 0, 3, 12]
    s.moveZeroes(data)
    print(data)
