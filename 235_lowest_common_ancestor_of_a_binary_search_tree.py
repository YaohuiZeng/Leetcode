# -*- coding: utf-8 -*-

"""

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the
lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”


        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5

For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since
a node can be a descendant of itself according to the LCA definition.

"""

"""
Q:
    (1) "two given nodes in BST": means that they indeed exist in BST and we can always find them? Yes
    (2) so it means at least two nodes in BST? Yes
    (3) could the two nodes be the same?
    (4) duplicate values in BST ?

Observation:
    (1) LCA is the node that i) is in the intersection set of two paths to the two node; and ii) has the smallest value.
    (2) in other words, LCA is the last node shared by the two search paths towards the two given nodes.

Algorithm: Time: O(n) because in worst case well will traverse all nodes to get the path; Space: O(n)
    (1) first find a path to node p, put all nodes along the path into queue.
    (2) then when searching for q, each time check whether current node is the first node in queue. If so, set that to be LCA. Then dequeue(), and set current node to be its left/right based on value comparison; Otherwise, stop, return LCA.
            Note: in (2) if current node has the same value as q; then return current node as LCA. (assume no duplicate values??)

"""


from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        queue = deque()

        cur_node = root
        found = False
        while not found:
            queue.append(cur_node)
            if cur_node.val < p.val:
                cur_node = cur_node.right
            elif cur_node.val > p.val:
                cur_node = cur_node.left
            else:
                found = True

        cur_node = root
        while queue and cur_node is queue[0]:
            LCA = queue.popleft()
            if cur_node.val < q.val:
                cur_node = cur_node.right
            elif cur_node.val > q.val:
                cur_node = cur_node.left
            else:
                return cur_node

        return LCA


    def lowestCommonAncestor2(self, root, p, q):
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor2(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor2(root.right, p, q)
        else:
            return root


