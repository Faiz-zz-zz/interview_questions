"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        memo = {}
        def find_next(string, ind):
            if string == "": return True
            if ind in memo: return memo[ind]
            valid = False

            for i in range(len(string)):
                sub_string = string[:i + 1]
                if sub_string in wordDict:
                    valid = valid or find_next(string[i + 1:], i + 1)
            memo[ind] = valid
            return valid

        if s == "": return False

        return find_next(s, 0)
        
