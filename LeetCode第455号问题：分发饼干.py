# encoding:utf8
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        result = 0
        # 从小到大的顺序使用各个糖果s尝试每个孩子g
        i = 0
        j = 0
        len_g = len(g)
        len_s = len(s)
        while i < len_g and j < len_s:
            if s[j] >= g[i]:
                result += 1
                j += 1
                i += 1
            else:
                # 如果糖果比孩子小，需要更大的糖果
                j += 1
        # 如果糖果只尝试一次成功，就换下一个孩子，
        return result

if __name__ == "__main__":
    re = Solution()
    g = [10,9,8,7]
    s = [5,6,7,8]
    print re.findContentChildren(g, s)