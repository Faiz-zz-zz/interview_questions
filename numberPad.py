"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""



class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        
        """
        
        if digits == "":
            return []
        pad = {"0":" ", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        array = []
        
        self.recurMethod("", array, pad, digits)
        return array
        
    def recurMethod(self, wordSoFar, array, pad, digits):
        if len(digits) == 1:
            for letter in pad[digits[0]]:
                array.append(wordSoFar + letter)
        
        else:
            for letter in pad[digits[0]]:
                self.recurMethod(wordSoFar + letter, array, pad, digits[1:])
obj = Solution()

print(obj.letterCombinations("733662"))