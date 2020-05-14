class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        data_dict = {}
        for index, num in enumerate(nums):
            if num in data_dict:
                if index - data_dict[num] <= k:
                    return True
                data_dict[num] = index
            data_dict[num] = index
        return False


if __name__ == '__main__':
    data = [1, 0, 1, 1]
    s = Solution()
    print(s.containsNearbyDuplicate(data, 1))
