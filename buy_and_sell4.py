class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        loc = [0 for i in range(k + 1)]
        glob = [0 for i in range(k + 1)]

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k + 1):
                    loc[j] = max(glob[j - 1] + max(diff, 0), loc[j] + diff)
                    glob[j] = max(glob[i], loc[j])
        return glob[-1]            
print(Solution().maxProfit(5, ))
