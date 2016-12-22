"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        retDict = {}

        for word in strs:
            keyValue = ''.join(list(sorted(list(word))))
            if keyValue in retDict.keys():
                retDict[keyValue].append(word)
            else:
                retDict[keyValue] = [word]
        return [retDict[key] for key in retDict.keys()]


obj = Solution()

print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
