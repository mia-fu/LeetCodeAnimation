# encoding:utf8
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = s[1]
        s_start = s.index(s1)
        s_end = s.rindex(s1)
        print s_start
        print s_end

if __name__ == '__main__':
    s = Solution()
    nums = "cbcbd"
    print s.longestPalindrome(nums)
