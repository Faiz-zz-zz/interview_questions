"""
Given a string s, partition s such that every substring of
 the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning
 of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could
 be produced using 1 cut.
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        if s is None or len(s) <= 1:
            return 0
        m = len(s)
        dp = [[False] * m for i in range(m)]
        for width in range(m):
            for i in range(m - width):
                j = i + width
                dp[i][j] = (width <= 1 or dp[i + 1][j - 1]) and s[i] == s[j]
        dpp = [-1] * (m + 1)
        for i in range(m):
            minvalue = i
            for j in range(i + 1):
                if dp[j][i]:
                    minvalue = min(minvalue, dpp[j])
            dpp[i + 1] = minvalue + 1
        return dpp[-1]

print(Solution().minCut("abacbcd"))
