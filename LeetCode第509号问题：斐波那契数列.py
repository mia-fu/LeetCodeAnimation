class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = list(range(N + 1))
        for i in range(N + 1):
            if i < 2:
                result[i] = i
            else:
                result[i] = result[i - 1] + result[i - 2]

        return result[-1]

if __name__ == '__main__':
    s = Solution()
    print s.fib(100)
