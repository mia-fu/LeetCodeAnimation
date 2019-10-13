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
        head = ListNode(0)
        first = head
        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1
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

