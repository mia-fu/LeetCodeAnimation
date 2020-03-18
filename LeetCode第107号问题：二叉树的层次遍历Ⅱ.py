# encoding: utf-8
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        res = []
        while queue:
            alist = []
            for i in range(len(queue)):
                cur = queue.pop(0)
                alist.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(alist)
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    r1 = TreeNode(3)
    r2 = TreeNode(9)
    r3 = TreeNode(20)
    r4 = TreeNode(15)
    r5 = TreeNode(7)
    r1.left = r2
    r1.right = r3
    r3.left = r4
    r3.right = r5
    print s.levelOrderBottom(r1)
