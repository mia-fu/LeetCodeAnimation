# encoding:utf-8
class MaxQueue(object):

    def __init__(self):
        self.cur_max = -1
        self.cur_second = -1
        self.queue = []

    def max_value(self):
        """
        :rtype: int
        """
        return self.cur_max

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value > self.cur_max:
            self.cur_second = self.cur_max
            self.cur_max = value
        elif self.cur_second > 0 and value > self.cur_second:
            self.cur_second = value
        self.queue.append(value)

        return None

    def pop_front(self):
        """
        :rtype: int

        """
        if not self.queue: return -1
        var = self.queue.pop(0)
        if var == self.cur_max:
            if self.cur_second == -1:
                # 需要重新计算max和second
                self.cur_max = -1
                for val in self.queue:
                    if val >= self.cur_max:
                        self.cur_second = self.cur_max
                        self.cur_max = val
                    elif val > self.cur_second:
                        self.cur_second = val
            else:
                self.cur_max = self.cur_second
                self.cur_second = -1
        elif var == self.cur_second:
            self.cur_second = -1
        return var


"""
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

"""

# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
param_1 = obj.max_value()
value = [[], [1], [2], [], [], []]
print obj.push_back([1])
print obj.push_back([2])
print obj.max_value()
print obj.pop_front()
print obj.max_value()
param_3 = obj.pop_front()
