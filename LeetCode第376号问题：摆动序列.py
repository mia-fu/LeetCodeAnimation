# encoding:utf8

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        up = 1
        down = 1
        # 摆动序列，波峰和波谷的差值最多为1

        for i in range(1, len(nums)):
            # 如果该数比前一个数大，说明是从封底到封顶的
            if nums[i] > nums[i - 1]:
                up = down + 1
            if nums[i] < nums[i - 1]:
                down = up + 1

        return max(up, down)

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5,6,7,8,9]
    print s.wiggleMaxLength(nums)