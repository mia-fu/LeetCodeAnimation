# encoding:utf8

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        f = [1] * n

        if n <= 1:
            return n
        # 遍历整个nums长度 从第二个元素开始往前比
        for i in range(1, n):
            # 值比较比i前面的元素
            for j in range(i):
                # 如果前面的元素比后面的元素小，这个是上升序列，
                if nums[j] < nums[i]:
                    # 在上升序列中，看前面的元素是否有大元素， + 1
                    f[i] = max(f[i], f[j] + 1)

        return max(f)


if __name__ == "__main__":
    s = Solution()
    nums = [10,9,2,5,3,11]
    print s.lengthOfLIS(nums)