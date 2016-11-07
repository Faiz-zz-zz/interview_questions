"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = [None for _ in range(len(s))]
        right = [None for _ in range(len(s))]
        hash = {}
        for ind, letter in enumerate(s[::-1]):
            if letter in hash:
                hash[letter] += 1
            else:
                hash[letter] = 1
            right[len(s) - ind - 1] = dict(hash)
        hash = {}
        for ind, letter in enumerate(s):
            if letter in hash:
                hash[letter] += 1
            else:
                hash[letter] = 1
            left[ind] = dict(hash)
            maxima = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                keys = list(set(left[i].keys()) & set(right[j].keys()))
                sub_map = {t: min(left[i][t], right[j][t]) for t in keys}
                if all(map(lambda x: x >= k, sub_map.values())):
                    print(sub_map)
                    print(s[i:j+1])
                    maxima = max(maxima, j - i + 1)
        return maxima
print(Solution().longestSubstring("aaabb", 2))
