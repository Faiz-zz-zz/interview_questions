"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""

class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		thePair = [[prices[0], prices[0]], prices[0]]
		for num in prices:
			if num < thePair[1]:
				thePair[1] = num
			else:
				if num > thePair[1]:
					if (num - thePair[1]) > (thePair[0][1] - thePair[0][0]):
						thePair[0][0] = thePair[1]
						thePair[0][1] = num
					elif thePair[0][1] - thePair[0][0] < num - thePair[0][0]:
						thePair[0][1] = num
		return thePair[0][1] - thePair[0][0]
			
obj = Solution()

print(obj.maxProfit([5, 4, 3, 2, 1]))            				  