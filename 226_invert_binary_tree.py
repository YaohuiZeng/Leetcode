"""

Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1


"""

"""

Algorithm: Time: O(n), space: O(n): bad!!
    (1) use queue do level-traversal; put all into stack
    (2) pop out from stack, check if leaves, do nothing; else, invert.

Algorithm 2: Time: O(n), space: O(n)
    (1) use stack do in-order traversal
    (2) Alarm: when poping out current node from stack, before inverting its subtrees, need to store its right node. Then invert, then set current node to its right node.

Algorithm 3: Time: O(n), space: O(n)
    (1) use queue to level-order traversal; iterative

Algorithm 4: recursive. Time: O(n); space: O(n)
    (1) Because of recursion, O(h) function calls will be placed on the stack in the worst case, where h is the height of the tree. Because h in O(n), the space complexity is O(n).

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

    def invertTree_queue(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # soln 3: queue, iterative
        if root is None:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

    def invertTree_stack(self, root):

        if root is None:
            return None

        stack = []
        cur_node = root
        done = False

        while not done:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                if stack:
                    cur_node = stack.pop()
                    cur_node.left, cur_node.right = cur_node.right, cur_node.left  # swap left and right
                    cur_node = cur_node.left  # now go to original right subtree, which is current left subtree
                else:
                    done = True
        return root

    def invertTree_recursive(self, root):
        if root is None:
            return None

        root.left, root.right = self.invertTree_recursive(root.right), self.invertTree_recursive(root.left)
        return root

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

    s = Solution()

    s.print_levelorder(root)
    print "End\n"

    print s.print_levelorder(s.invertTree_queue(root))
    print s.print_levelorder(s.invertTree_stack(root))
    print s.print_levelorder(s.invertTree_recursive(root))