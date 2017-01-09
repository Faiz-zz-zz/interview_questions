"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return findWords(0, len(s), s, wordDict, {})

def findWords(start, end, s, wordDict, cache):
    if start in cache:
        return cache[start]
    cache[start] = []
    candidate = ''
    current = start
    while current < end:
        candidate += s[current]
        current += 1
        if candidate in wordDict:
            if current == end:
                cache[start].append(candidate)
            else:
                for x in findWords(current, end, s, wordDict, cache):
                    cache[start].append(candidate + ' ' + x)
    return cache[start]


        
