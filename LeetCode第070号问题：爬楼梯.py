# encoding:utf-8
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+2)
        dp[1] = 1
        dp[2] = 2
        if n == 1 or n == 2:
            return dp[n]
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    n = 1
    print (s.climbStairs(n))