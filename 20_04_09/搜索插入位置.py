class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        '''
        工程化代码
        :param nums:
        :param target:
        :return:
        '''
        if target not in nums:
            nums.append(target)
            nums = sorted(nums)
        return nums.index(target)

    def searchInsert2(self, nums: [int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start


if __name__ == '__main__':
    a = [1, 3, 6, 7, 9, 15]
    s = Solution()
    result = s.searchInsert2(a, 4)
    print(result)
