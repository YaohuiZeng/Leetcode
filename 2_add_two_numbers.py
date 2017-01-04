"""

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each
of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        tmp = l1.val + l2.val

        if tmp < 10:
            lr = ListNode(tmp)
            carryover = 0
        else:
            lr = ListNode(tmp - 10)
            carryover = 1

        cur = lr
        while l1.next and l2.next:
            tmp = l1.next.val + l2.next.val + carryover
            if tmp < 10:
                cur.next = ListNode(tmp)
                carryover = 0
            else:
                cur.next = ListNode(tmp - 10)
                carryover = 1
            l1, l2, cur = l1.next, l2.next, cur.next

        while l1.next:
            tmp = l1.next.val + carryover
            if tmp < 10:
                cur.next = ListNode(tmp)
                carryover = 0
            else:
                cur.next = ListNode(tmp - 10)
                carryover = 1
            l1, cur = l1.next, cur.next

        while l2.next:
            tmp = l2.next.val + carryover
            if tmp < 10:
                cur.next = ListNode(tmp)
                carryover = 0
            else:
                cur.next = ListNode(tmp - 10)
                carryover = 1
            l2, cur = l2.next, cur.next

        if carryover:
            cur.next = ListNode(1)
            cur.next.next = None
        else:
            cur.next = None
        return lr

    def addTwoNumbers2(self, l1, l2):

        # soln 2: use dummy node

        dummy = ListNode(0)
        carryover = 0
        cur = dummy

        while l1 or l2:
            val = carryover
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            val, carryover = val % 10, val // 10
            cur.next = ListNode(val)
            cur = cur.next

        if carryover:
            cur.next = ListNode(1)
            cur.next.next = None
        else:
            cur.next = None
        return dummy.next


if __name__ == "__main__":
    num1, num1.next, num1.next.next = ListNode(6), ListNode(3), ListNode(5)
    num2, num2.next, num2.next.next = ListNode(5), ListNode(6), ListNode(4)

    print num1
    print num2
    print Solution().addTwoNumbers(num1, num2)
    print Solution().addTwoNumbers2(num1, num2)



