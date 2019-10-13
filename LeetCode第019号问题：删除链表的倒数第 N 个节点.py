# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for i in range(n):
            if fast.next:
                fast = fast.next
            else:
                return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

if __name__ == "__main__":
    head = ListNode(1)
    n = 1
    p = Solution()
    p = p.removeNthFromEnd(head, n)
    while p:
        print p.val
        p = p.next