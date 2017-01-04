"""

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


"""


from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def print_levelorder(self, root):
        if root is None:
            return
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            print node.val, "->",
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


    # Time: O(n); Space: O(1)
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))




if __name__ == "__main__":
    root = TreeNode(0)
    node2 = TreeNode(-4)
    node3 = TreeNode(-3)
    root.left, root.right = node2, node3

    node4 = TreeNode(-1)
    node2.right = node4

    node5 = TreeNode(8)
    node3.left = node5

    node6 = TreeNode(3)
    node4.right = node6

    node7 = TreeNode(9)
    node5.right = node7

    node8 = TreeNode(-2)
    node6.left = node8

    node9 = TreeNode(4)
    node7.left = node9

    Solution().print_levelorder(root)
    print "End\n"

    print Solution().maxDepth(root)
