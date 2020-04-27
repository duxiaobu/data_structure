class Solution:
    def generate(self, num_rows):
        result = []
        for num in range(num_rows):
            row = [None for _ in range(num + 1)]
            # 每一列的第一位和最后一位都是1
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = result[num - 1][j - 1] + result[num - 1][j]
            result.append(row)
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.generate(5)
    print(result)
