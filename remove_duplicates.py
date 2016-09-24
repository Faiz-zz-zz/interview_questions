"""Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3."""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		seenDict = {}

		node = head

		while node != None:
			if node.val in seenDict:
				seenDict[node.val] += 1
			else:
				seenDict[node.val] = 1

			node = node.next
		
		node = head

		for i in seenDict.keys():
			if seenDict[i] > 1:
				seenDict.pop(i, None)
				
		if len(seenDict) == 0:
			return None
		else:
			keys = seenDict.keys()

			head = ListNode(keys[0])
			node = head
			for i in keys[1:]:
				node.next = ListNode(i)
				node = node.next
		return head		