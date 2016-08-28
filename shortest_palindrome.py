"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

"""

class Solution(object):
	def shortestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		for i in reversed(range(len(s) + 1)):
			pal = s[i:][::-1] + s
			if pal == pal[::-1]:
				return pal
print(Solution().shortestPalindrome(a))				
