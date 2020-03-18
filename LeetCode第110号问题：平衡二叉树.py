# encoding:utf-8
# Definition for a binary tree node.

"""
是平衡二叉树的条件：
左子树是平衡二叉树。
右子树是平衡二叉树。
左右子树之间的深度不超过1.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False

        depth_left, depth_right = self.depth(root.left), self.depth(root.right)
        if abs(depth_left - depth_right) >= 2:
            return False
        else:
            return True







if __name__ == "__main__":
    root = TreeNode("1")
    h1 = TreeNode("2")
    h2 = TreeNode("3")
    h3 = TreeNode("4")
    h4 = TreeNode("5")

    root.left = h1
    root.right = h2
    h1.left = h3
    h1.right = h4
    s = Solution()
    print s.isBalanced(root)
