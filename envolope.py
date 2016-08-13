""" 
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
import sys
import math
class Solution(object):
	
	def helper(self, envelopes, last, memo):
		print last
		if len(envelopes) == 0:
			return 0

		if memo[len(envelopes)] != None:
			return memo[len(envelopes)]	
		
		if len(envelopes) == 1:
			if envelopes[0][0] < last[0] and envelopes[0][1] < last[1]:
				return 1
			else:
				return 0

		one = 0
		two = 0

		if (envelopes[0][0] < last[0]  and envelopes[0][1] < last[1]):
			one = 1 + self.helper(envelopes[1:], envelopes[0], memo)
			two = 0 + self.helper(envelopes[1:], last, memo)
			memo[len(envelopes)] = max(one, two)
			return max(one, two)
		else:
			memo[len(envelopes)] = self.helper(envelopes[1:], last, memo)
			return memo[len(envelopes)]

	def maxEnvelopes(self, envelopes):
		"""
		:type envelopes: List[List[int]]
		:rtype: int
		"""
		memo = {i:None for i in range(1, len(envelopes)+1)}
		envelopes.sort(key = lambda k : math.sqrt(k[0]**2 + k[1]**2))
		print envelopes
		envelopes.reverse()
		total = self.helper(envelopes, [100,100], memo)
		
		if len(envelopes) == 0:
			return 0
		
		return total 

obj = Solution()

print(obj.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))        		
