class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return list(map(s.index, s)) == list(map(t.index, t))


if __name__ == '__main__':
    x = 'egg'
    y = 'aab'
    print(list(map(x.index, x)))
    print(list(map(y.index, y)))
