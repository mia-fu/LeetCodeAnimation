# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False


if __name__ == "__main__":
    h1 = TreeNode("1")
    h2 = TreeNode("2")
    h3 = TreeNode("3")

    t1 = TreeNode("1")
    t2 = TreeNode("2")
    t3 = TreeNode("3")

    h1.left = h2
    h1.right = h3

    t1.left = t2

    s = Solution()
    print s.isSameTree(h1, t1)
