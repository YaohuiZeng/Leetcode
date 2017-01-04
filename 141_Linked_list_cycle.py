"""

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        d = dict()
        if not head:
            return False
        d[head] = 1
        node = head.next
        while node:
            if node in d:
                return True
            else:
                d[node] = 1
                node = node.next
        return False

    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False



