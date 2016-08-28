"""Given a singly linked list, determine if it is a palindrome."""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        array = []

        while head != None:
        	array.append(str(head.val))
        	head = head.next
        if len(array) <= 1:
            return True
        return array == array[::-1]