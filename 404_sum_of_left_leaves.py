"""

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


"""

"""
Q:
    (1) is root alone a left leave? No!!!

Algorithm: (recursive) depth-search first. Time: O(n); Space: O(1)
    (1) if node is not None:
            then check whether its left subtree is leaf:
                if true, add up to result, otherwise recursively search its left subtree.
            then recursively search its right subtree

Algorithm 2: (preferred) pass a flag to indicate whether the leaf is left or right. If left, return its value, otherwise
 return 0. Time: O(n). Space: O(1)

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if root is not None:
            if self.is_leaf(root.left):
                res += root.left.val
            else:
                res += self.sumOfLeftLeaves(root.left)

            res += self.sumOfLeftLeaves(root.right)

        return res

    def is_leaf(self, node):
        if node is None:
            return False
        if node.left is None and node.right is None:
            return True
        return False

    def sumOfLeftLeaves2(self, root):
        def sumOfLeftLeavesHelper(root, is_left):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return root.val if is_left else 0
            else:
                return sumOfLeftLeavesHelper(root.left, True) + sumOfLeftLeavesHelper(root.right, False)

        return sumOfLeftLeavesHelper(root, False)

