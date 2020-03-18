# encoding:utf8
class Solution(object):
    def bag01(self, weights, values, capacity):
        # 动态规划
        n = len(weights)
        result = [[0 for j in range(capacity + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                result[i][j] = result[i - 1][j]
                # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
                if j >= weights[i - 1] and result[i][j] < result[i - 1][j - weights[i - 1]] + values[i - 1]:
                    result[i][j] = result[i - 1][j - weights[i - 1]] + values[i - 1]
        for x in result:
            print(x)
        return result

    def show(self, weights, capacity, result):
        n = len(weights)
        print ('最大解为：{}'.format(result[n][capacity]))
        x = [False for i in range(n + 1)]
        j = capacity
        for i in range(n, 0, -1):
            if result[i][j] > result[i - 1][j]:
                # i代表第i个物品，如果放入第i个物品的价值大于同等重量放入i-1物品的重量，说明选择了物品i
                x[i] = True
                j -= weights[i - 1]
        print('items:')
        for i in range(n + 1):
            if x[i]:
                print('no:{}'.format(i))


if __name__ == '__main__':
    s = Solution()
    weights = [2, 2, 3, 1, 5, 2]
    values = [2, 3, 1, 5, 4, 3]
    capacity = 10
    result = s.bag01(weights, values, capacity)
    s.show(weights, capacity, result)
