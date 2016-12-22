"""

Say you have an array for which the ith element is the price of a given
 stock on day i.

Design an algorithm to find the maximum profit. You may complete at most
 two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must
 sell the stock before you buy again).
"""


class Solution(object):
    def maxProfit(self, prices):
        right = []
        left = []
        for i in range(len(prices)):
            right.append(self.single(prices[i:]))
            left.append(self.single(prices[:i]))

        return max(map(lambda k: k[0] + k[1], list(zip(right, left))))

    def single(self, prices):
        if prices == []:
            return 0
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


	def maxProfit2(self, prices):

		if prices == []:
			return 0
		left = [0]*len(prices)
		right = [0]*len(prices)

		minima = prices[0]
		for i in range(1, len(prices)):
			minima = min(minima, prices[i])
			left[i] = max(left[i - 1], prices[i] - minima)

		maxima = prices[-1]
		for i in range(len(prices) - 2, -1, -1):
			maxima = max(maxima, prices[i])
			print(maxima)
			right[i] = max(right[i + 1], maxima - prices[i])
		print(left, right)
		maxpro = 0
		for i in range(len(prices)):
			maxpro = max(maxpro, left[i] + right[i])
		print("yoyoy")
		return maxpro

obj = Solution()
print(obj.maxProfit2([1]))
