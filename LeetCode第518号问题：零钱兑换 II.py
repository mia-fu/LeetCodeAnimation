# encoding:utf8
class Solution:
    def change(self, amount, coins):
        if not coins:
            # 两个case 如果没有硬币， 而且金额数为0， 返回1。 否则返回0，为不能凑成总金额
            if amount == 0:
                return 1
            if amount > 0:
                return 0

        # amount 表示背包大小 列， n 表示硬币数量 行
        n = len(coins)
        # dp[i][j] j表示金额 i表示使用到集中硬币
        dp = [0 for i in range(amount + 1)]
        print(dp)

        # 初始化列的第一个数字为均1
        dp[0] = 1

        # 单独初始化第一行
        i = coins[0]
        while i <= amount:
            dp[i] = 1
            i += coins[0]

        # print(dp)
        for i in range(1, n):
            for j in range(1, amount + 1):
                # 如果背包容量小于商品数值，不能放入。只加上上一个硬币的数量即可
                dp[j] += dp[j-coins[i]]

        print(dp)
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    coins = [1, 2, 5]
    amount = 5
    print (s.change(amount, coins))