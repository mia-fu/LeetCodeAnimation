# encoding:utf8
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'{': '}', '[': ']', '(': ')', '?':'?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1



if __name__ == "__main__":
    s = Solution()
    print s.isValid(']')