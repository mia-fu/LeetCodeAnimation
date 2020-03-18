#encoding:utf8
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False

        capacity = s // 2
        result = [[False for j in range(capacity + 1)] for i in range(n + 1)]

        # 先填第一行，只让第一个数放在是他容量为1的地方
        if nums[0] <= capacity:
            result[0][nums[0]] = True

        # 再从表格的第二行开始填
        for i in range(1, n):
            for j in range(capacity + 1):
                # 先讲上面的数据抄录下来，再进行修正
                result[i][j] = result[i - 1][j]
                if (nums[i] == j):
                    result[i][j] = True
                    continue
                if nums[i] < j:
                    result[i][j] = result[i - 1][j] or result[i - 1][j - nums[i]]
        return result[n - 1][capacity]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 5, 11, 5]
    print s.canPartition(nums)
