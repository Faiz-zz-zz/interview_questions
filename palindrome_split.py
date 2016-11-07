"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = {}

        def dfs(string):
            print(string, "This starts here")
            if not string:
                return []
            if string in result:
                return result[string]
            ret_array = []
            for i in range(len(string)):
                if string[:i+1] == string[:i+1][::-1]:
                    parts = dfs(string[i+1:])
                    if len(parts) > 0:
                        for part in parts:
                            ret_array.append([string[:i+1]] + part)
                    else:
                        ret_array.append([string[:i+1]])
            result[string] = ret_array
            return ret_array
        dfs(s)
        return result[s]
print(Solution().partition("aab"))
