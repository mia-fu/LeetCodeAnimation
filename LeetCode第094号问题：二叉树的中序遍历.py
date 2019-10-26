# encoding:utf-8
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        cur = root
        res = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            res.append(node.val)
            cur = node.right
        return res


if __name__ == "__main__":
    root = TreeNode("A")
    h1 = TreeNode("B")
    h2 = TreeNode("C")
    h3 = TreeNode("D")
    h4 = TreeNode("E")
    h5 = TreeNode("F")
    h6 = TreeNode("G")
    root.left = h1
    root.right = h2
    h1.left = h3
    h1.right = h4
    h2.left = h5
    h2.right = h6
    s = Solution()
    print s.inorderTraversal(root)
