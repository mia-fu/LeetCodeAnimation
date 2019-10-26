# encoding:utf-8
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = [root]  # 只用来存放根节点值
        cur = root
        res = []    # 用来存放所有结点值
        if not cur:
            return []
        while queue:
            size = len(queue)
            temp = []
            for x in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node.val)
            res.append(temp)
        return res




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
    print s.levelOrder(root)
