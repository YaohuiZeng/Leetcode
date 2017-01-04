"""

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?


"""

"""
Q:
    (1) return list of values

Algorithm: Time: O(n); Space: O(n)
    (1) recursive

Algorithm 2: Time: O(n); Space: O(n)
    (1) iterative using stack

"""


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

        res = []
        if root is None:
            return []
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))

        return res


    def inorderTraversal2(self, root):
        res, stack = [], []
        cur_node = root
        done = False
        while not done:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            elif stack:
                cur_node = stack.pop()
                res.append(cur_node.val)
                cur_node = cur_node.right
            else:
                done = True

        return res