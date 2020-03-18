class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        flag = True
        if x < 0:
            return False
        else:
            y = str(x)
            y = y[::-1]
            if y == str(x):
                return True
            else:
                return False




if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(123)