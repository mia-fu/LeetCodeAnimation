# encoding:utf-8
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hour = [1, 2, 4, 8]
        minute = [1, 2, 4, 8, 16, 32]
        h_len, m_len = len(hour), len(minute)
        res = []

        def time(combination, led, start):
            if led == 0:
                if combination[1] < 10:
                    res.append(str(combination[0]) + ':0' + str(combination[1]))
                else:
                    res.append(str(combination[0]) + ':' + str(combination[1]))
            else:
                for i in range(start, h_len + m_len):
                    if i < h_len:
                        combination[0] += hour[i]
                        if combination[0] < 12:
                            time(combination, led - 1, i + 1)
                        combination[0] -= hour[i]
                    else:
                        combination[1] += minute[i - h_len]
                        if combination[1] < 60:
                            time(combination, led - 1, i + 1)
                        combination[1] -= minute[i - h_len]

        cur = [0] * 2
        time(cur, num, 0)
        return res



if __name__ == '__main__':
    n = 1
    s = Solution()
    print s.readBinaryWatch(n)
