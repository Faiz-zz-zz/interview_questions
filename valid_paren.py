"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {"(":")", "{":"}", "[":"]"}
        
        stack = []
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(dic[i])
            else:
                if len(stack) != 0:
                    if i == stack[len(stack) - 1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) != 0:
            return False
        else:    
            return True            
                   
		

obj = Solution()

print(obj.isValid('()'))        