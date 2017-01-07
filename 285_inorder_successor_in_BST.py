"""

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

"""

"""
Q:
    (1) what if the node is the first one in in-order traversal? return None
    (2) always assume p is a node in BST?

Algorithm:
    (1) in-order traversal, compare where current node is equal to given node, if true, return 'next' node

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        stack = []
        cur = root
        done, flag = False, False
        while not done:
            if cur:
                stack.append(cur)
                cur = cur.left
            elif stack:
                cur = stack.pop()
                if flag:
                    return cur
                if cur == p:
                    flag = True
                cur = cur.right
            else:
                done = True
        return None

    # compact way of soln 1
    def inorderSuccessor2(self, root, p):
        stack, flag = [], False
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if flag:
                return root
            if root == p:
                flag = True
            root = root.right
        return None


if __name__ == "__main__":

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    print Solution().inorderSuccessor(root, root.left.right).val
    print Solution().inorderSuccessor2(root, root.left.right).val

    print Solution().inorderSuccessor(root, root.right.left).val
    print Solution().inorderSuccessor2(root, root.right.left).val

    print Solution().inorderSuccessor(root, root.right.right)
    print Solution().inorderSuccessor2(root, root.right.right)

