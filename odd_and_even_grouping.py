"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = second = head
        while second is not None:
            if not second.val % 2:
                second = second.next
            else:
                first.val, second.val = second.val, first.val
                first = first.next
                second = second.next
        return head


num1 = ListNode(1)
num2 = ListNode(2)
num3 = ListNode(3)
num4 = ListNode(4)
num5 = ListNode(5)

num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num5
num5.next = None

a = Solution().oddEvenList(num1)
while a:
    print(a.val)
    a = a.next
