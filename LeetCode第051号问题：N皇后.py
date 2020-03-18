# encoding:utf8
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []

        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return
            for q in range(n):
                """
                不在主对角线上： xi-i ≠ xj-j
                不在负对角线上： xi+i ≠ xj+j
                """
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        DFS([], [], [])
        """
        输出：'Q' 和 '.' 分别代表了皇后和空位
        """

        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]




def main():
    n = int(input("请输入皇后的个数："))
    print("\n请按照如下提示摆放皇后：")
    s = Solution()
    cnt = s.solveNQueens(n)
    print cnt


if __name__ == '__main__':
    main()
