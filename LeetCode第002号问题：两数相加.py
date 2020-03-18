class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        val = l1.val + l2.val
        result = ListNode(val % 10)
        result.next = self.addTwoNumbers(l1.next, l2.next)

        if val >= 10:
            result.next = self.addTwoNumbers(result.next, ListNode(1))
        return result





if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    result = s.addTwoNumbers(l1, l2)

    while result:
        print result.val
        result = result.next
