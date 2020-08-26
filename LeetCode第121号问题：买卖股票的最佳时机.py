# encoding:utf-8
class Solution:
    def maxProfit(self, prices):
        # 动态规划 前i天的最大收益 = max{前i-1天的最大收益, 第i天的(卖出)价格 - 前i-1天中的最小(买入)价格}

        if not prices:
            return 0

        max_p = 0
        min_p = prices[0]

        for i in range(1, len(prices)):
            max_p = max(max_p, prices[i] - min_p)
            min_p = min(min_p, prices[i])

        return max_p

if __name__ == "__main__":
    s = Solution()
    prices = [7,1,5,3,6,4]
    res = s.maxProfit(prices)
    print(res)