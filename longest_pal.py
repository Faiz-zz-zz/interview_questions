"longest palindrome substring"

# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         dp = [[False for i in range(len(s))] for j in range(len(s))]
#         for i in range(len(s)):
#             for j in range(len(s)):
#                 if j >= i: dp[i][j] = True
#         for i in range(len(s)):
#             for j in range(len(s)):
#                 dp[i][j] = (((j - i + 1) < 2) or dp[i + 1][j - 1]) and (s[i] == s[j])
#         maxima = (0, 0)
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if dp[i][j]:
#                     if (j - i + 1) > maxima[1] - maxima[0] + 1:
#                         maxima = (i, j)
#         return s[maxima[0]: maxima[1] + 1]
# print(Solution().longestPalindrome("bb"))

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # m = len(s)
        # dp = [[False for i in range(len(s))] for j in range(len(s))]
        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         if j >= i: dp[i][j] = True
        # dp = [[False] * m for i in range(m)]
        # for width in range(m):
        #     for i in range(m - width):
        #         j = i + width
        #         dp[i][j] = (width <= 1 or dp[i + 1][j - 1]) and s[i] == s[j]
        # maxima = (0, 0)
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if dp[i][j]:
        #             if (j - i + 1) > maxima[1] - maxima[0] + 1:
        #                 maxima = (i, j)
        #
        # return s[maxima[0]: maxima[1] + 1]
        # bruteborce
        # maxima = (0, 0)
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if s[i:j+1] == s[i:j+1][::-1]:
        #             if maxima[1] - maxima[0] + 1 < j - i + 1:
        #                 maxima = (i, j)
        # return s[maxima[0]: maxima[1] + 1]

        def expand_from_centre(s, c1, c2):
            l, r = c1, c2
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        longest = s[0:1]
        for i in range(len(s) - 1):
            sub = expand_from_centre(s, i, i)
            if len(sub) > len(longest):
                longest = sub

            sub = expand_from_centre(s, i, i + 1)
            if len(sub) > len(longest):
                longest = sub

        return longest

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        array = [i**2 for i in range(1, n + 1)]

        matrix = [[None for i in range(n)] for j in range(n)]
        p = 0
        rowStart, rowEnd, colStart, colEnd = 0, 0, n - 1, n - 1

        while rowStart <= rowEnd and colStart <= colEnd:
            # Top
            for i in range(colStart, colEnd + 1):
                matrix[rowStart][i] = matrix[p]
                p += 1
            rowStart += 1

            for i in range(rowStart, rowEnd + 1):
                matrix[colEnd][i] = matrix[p]
                p += 1
            colEnd -= 1

            if colStart <= colEnd:
                for i in range(colEnd, colStart - 1, -1):
                    matrix[rowEnd][i] = matrix[p]
                    p += 1
            rowEnd -= 1

            if rowStart <= rowEnd:
                for i in range(rowEnd, rowStart - 1, -1):
                    matrix[colStart][i] = matrix[p]
                    p += 1
             colStart += 1

        return matrix


print(Solution().longestPalindrome("malayalam"))
