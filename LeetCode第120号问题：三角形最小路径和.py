# encoding:utf-8
class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        m = len(triangle)
        # dp 只保存行上的数，自底向上 滚动数组，到dp[0]到顶，返回最小数。
        dp = [[0] * (m+1) for _ in range(m + 1)]
        print(dp)
        # 贪心算法，找出最小值
        # dp[][] 表示当前位置上的最小路径
        for i in range(m - 1, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]

if __name__ == "__main__":
    s = Solution()
    tri = [[2],[3,4],[6,5,7],[4,1,8,3]]
    res = s.minimumTotal(tri)
    print(res)