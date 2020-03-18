# encoding:utf8
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            xstr = str(x)
            xstr = xstr[::-1]
            x = int(xstr)
        else:
            xstr = str(-x)
            xstr = xstr[::-1]
            x = -int(xstr)
        if -2 ** 31 < x < 2 ** 31 - 1:
            return x
        return 0
if __name__ == "__main__":
    s = Solution()
    print s.reverse(1563847412)