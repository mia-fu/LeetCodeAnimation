# encoding:utf8
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int m为行数
        :type n: int n为列数
        :rtype: int
        """
        result = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = result[i][j - 1] + result[i - 1][j]
        return result[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print s.uniquePaths(3, 7)
