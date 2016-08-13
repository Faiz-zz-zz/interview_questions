"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

"""

class Solution(object):
	def removeInvalidParentheses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		def isValid(string):
			ctr = 0
			for i in string:
				if i == '(':
					ctr += 1
				elif i == ')':
					ctr -= 1
					if ctr < 0:
						return False
			return ctr == 0
		bfs = {s}
		while True:
			valid = filter(isvalid, bfs)
			if valid:
				return valid
			bfs = {s[:i] + s[i+1:] for s in bfs for i in range(len(s))}