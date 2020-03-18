class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hasmap = {}
        for ind, num in enumerate(nums):
            hasmap[num] = ind
        for i, num in enumerate(nums):
            j = hasmap.get(target - num)
            if j is not None and i != j:
                return [i,j]

if __name__ == "__main__":
    s = Solution()
    print s.twoSum([2, 7, 1, 29], 9)
