"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.
Try to do this in one pass.

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return None
        slow, fast = head, head  # deleted node is in btw slow and fast
        i = 1
        while i <= n:
            fast = fast.next
            i += 1
        if fast is None:  # meaning to delete head
            return head.next
        else:
            while fast.next is not None:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
        return head

    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy
        i = 1
        while i <= n:
            first = first.next
            i += 1
        while first.next is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
