# encoding:utf-8
"""
解释：
输入：inputs = ["RecentCounter","ping","ping","ping","ping"],
     inputs = [[],[1],[100],[3001],[3002]]
意思是， 在第1，100，3001，3002这四个时间点分别进行了ping请求，
在3001秒的时候， 他前面的3000秒指的是区间[1,3001]， 所以一共是有（1，100，3001）三个请求，
t = 3002的前3000秒指的是区间[2, 3002], 所以有100，3001，3002三次请求。
"""


class RecentCounter(object):

    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        while (len(self.queue) != 0) and (self.queue[0] < t - 3000):
            self.queue.pop(0)
        return len(self.queue)

if __name__ == "__main":
    r = RecentCounter()
    print r.ping(1)
    print r.ping(100)
    print r.ping(3001)
    print r.ping(3002)
    print r.ping(3002)

