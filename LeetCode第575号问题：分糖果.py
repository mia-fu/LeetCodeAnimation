#encoding:utf-8
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        """
        注意:
        数组的长度为[2, 10000]，并且确定为偶数。
        数组中数字的大小在范围[-100, 000, 100, 000]内。
        """
        len_c = len(candies) // 2
        if len_c == 1:
            return 1
        num = 0
        cur = []
        i = 0
        while len_c:
            if i >= len(candies):
                break
            if candies[i] not in cur:
                num += 1
                cur.append(candies[i])
                len_c -= 1
            i += 1
        return num


if __name__ == '__main__':
    candies = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    s = Solution()
    print s.distributeCandies(candies)
