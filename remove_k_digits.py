"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(num):
            while stack and k and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        return ''.join(stack[:-k or None]).lstrip('0') or '0'

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        while k:
            i = 0
            while i + 1 < len(num) and k and num[i] <= num[i + 1]:
                i += 1
            print(i)
            num = num[:i] + num[i+1:]
            k -= 1

        if num == "": return "0"
        num = str(int(num))
        return num
