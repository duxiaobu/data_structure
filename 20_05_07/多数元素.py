from collections import Counter


class Solution:
    def majorityElement(self, nums: [int]) -> int:
        # 字典保存
        result = {}
        for num in nums:
            if num not in result:
                result[num] = 1
            else:
                result[num] += 1
        tmp = sorted(result.items(), key=lambda x: x[1], reverse=True)
        return tmp[0][0]

    def majorityElement2(self, nums: [int]) -> int:
        # 投票法
        target = None
        count = 0
        for num in nums:
            if count == 0:
                target = num
            count += (1 if target == num else -1)
        return target


if __name__ == '__main__':
    s = Solution()
    data = [2, 2, 1, 3, 2, 1]
    print(s.majorityElement2(data))
    # print(s.majorityElement(data))
