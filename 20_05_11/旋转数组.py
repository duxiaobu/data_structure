class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        插入法
        """
        for i in range(k):
            nums.insert(0, nums.pop())

    def rotate2(self, nums: [int], k: int) -> None:
        """
        三次反转法
        """
        n = len(nums)
        k = k % n

        def swap(l: int, r: int):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        swap(0, n - k - 1)
        swap(n - k, n - 1)
        swap(0, n - 1)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 7, 8]
    s.rotate(nums, 2)
    print(nums)
