# encoding:utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        re = ListNode(0)
        first = re
        while l1 and l2:
            if l1.val > l2.val:
                re.next = l2
                l2 = l2.next
            else:
                re.next = l1
                l1 = l1.next
            re = re.next
        if l1 is None:
            re.next = l2
        if l2 is None:
            re.next = l1
        return first.next





if __name__ == "__main__":
    p10 = ListNode(2)
    p11 = ListNode(3)
    p20 = ListNode(1)
    p21 = ListNode(3)
    p22 = ListNode(4)
    p23 = ListNode(5)
    p10.next = p11

    p20.next = p21
    p21.next = p22
    p22.next = p23

    p = Solution()
    p = p.mergeTwoLists(p10, p20)
    while p:
        print p.val
        p = p.next

