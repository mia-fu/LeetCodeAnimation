# encoding:utf-8
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []  # 只用来存放根节点值
        cur = root
        res = []    # 用来存放所有结点值
        if not cur:
            return []
        while stack or cur:
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
            node = stack.pop()
            cur = node.right
        return res

    def preorderTraversal1(self, root):  # 递归
        res = []
        cur = root
        stack = []
        while stack or cur:
            if not cur:
                cur = stack.pop()
                cur = cur.right
            else:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
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
    print s.preorderTraversal1(root)
    print s.preorderTraversal(root)
