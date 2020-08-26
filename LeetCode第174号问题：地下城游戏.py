#encoding:utf8
class Solution:
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return None

        row = len(dungeon)  # 行
        colomn = len(dungeon[0])  # 列

        dp = [[float('inf')] * (colomn + 1) for _ in range(row + 1)]
        # dp[i][j] 表示这个点走到右下角所需的最小血量
        # 从右下角向左上角遍历，
        dp[row - 1][colomn] = 1
        dp[row][colomn - 1] = 1
        print(dp)
        # 如果右下角初始值为正，最低1
        # 如果右下角初始值为负，最低1或者比负的绝对值大1 max(1, 1-dp[-1][-1])

        for i in range(row - 1, -1, -1):
            for j in range(colomn - 1, -1, -1):
                # 从下往上
                if dungeon[i][j] >= dp[i + 1][j]:
                    dp[i][j] = 1
                elif dungeon[i][j] >= dp[i][j + 1]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i + 1][j] - dungeon[i][j], dp[i][j + 1] - dungeon[i][j])

        # print(dp)
        return(dp[0][0])



if __name__ == "__main__":
    s = Solution()
    dungeon = [[-1,1]]
    res = s.calculateMinimumHP(dungeon)
    print(res)