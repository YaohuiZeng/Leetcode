"""

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

"""

#
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         """
#         # solution 1: recursion
#         if head is None or head.next is None:
#             return head
#         else:
#             curr = head.next
#             next_next = head.next.next
#             head.next.next = head
#             head.next = self.swapPairs(next_next)
#         return curr
#         """
#         # solution 2: three pointers
#         dummy = ListNode(0)
#         dummy.next = head
#         curr = dummy
#         while curr.next and curr.next.next:
#             next_one, next_two, next_three = curr.next, curr.next.next, curr.next.next.next
#             curr.next = next_two
#             next_two.next = next_one
#             next_one.next = next_three
#             curr = next_one
#         return dummy.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            next_one, next_two, next_three = current.next, current.next.next, current.next.next.next
            current.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            current = next_one
        return dummy.next

    def swapPairs2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # solution 1: recursion
        if head is None or head.next is None:
            return head
        else:
            curr = head.next
            next_next = head.next.next
            head.next.next = head
            head.next = self.swapPairs(next_next)
        return curr


if __name__ == "__main__":
    head = ListNode(1)
    # head.next = ListNode(5)
    head.next, head.next.next, head.next.next.next = ListNode(5), ListNode(6), ListNode(2)
    print Solution().swapPairs2(head)
