# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        if root.left:
            for i in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + "->" + i)
        if root.right:
            for i in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + "->" + i)
        return paths



if __name__ == "__main__":
    root = TreeNode(1)
    h1 = TreeNode(2)
    h2 = TreeNode(3)
    h3 = TreeNode(5)
    root.left = h1
    root.right = h2
    h1.right = h3
    s = Solution()
    print s.binaryTreePaths(root)