class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        # 哈希法
        old_data = set()
        for num in nums:
            if num in old_data:
                return True
            old_data.add(num)
        return False


if __name__ == '__main__':
    pass
