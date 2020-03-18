#encoding:utf-8
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        head = 1
        tail = 2
        result = []

        while head < tail:
            sum = (tail + head) * (tail - head + 1) / 2
            cur = []
            if sum == target:
                for i in range(head, tail + 1):
                    cur.append(i)
                result.append(cur)
                head += 1
            else:
                if sum < target:
                    tail += 1
                else:
                    head += 1

        return result


if __name__ == "__main__":
    s = Solution()
    target = 15
    print s.findContinuousSequence(target)
