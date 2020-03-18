#encoding:utf8
class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        for i in range(n):
            A[m + i] = B[i]
        A.sort()
        return A


if __name__ == "__main__":
    s = Solution()
    A = [1, 2, 3, 0, 0, 0]
    m = 3
    B = [2, 5, 6]
    n = 3
    print s.merge(A, m, B, n)
