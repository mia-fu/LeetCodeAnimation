# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)

        return check(root, root)



if __name__ == "__main__":
    h1 = TreeNode("1")
    h2 = TreeNode("2")
    h3 = TreeNode("2")

    t1 = TreeNode("1")
    t2 = TreeNode("2")
    t3 = TreeNode("3")

    h1.left = h2
    h1.right = h3

    s = Solution()
    print s.isSymmetric(h1)
