"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		
		retArray = [("(", [n - 1, n])]
		for i in range(2*n - 1):
			array = []
			for item in retArray:
				if item[1][0] == 0 and item[1][1] == 0:
					pass
				elif item[1][0] > 0 and item[1][1] > 0 and item[1][0] < item[1][1]:
					array.append((item[0] + "(", [item[1][0]-1, item[1][1]]))
					array.append((item[0] + ")", [item[1][0], item[1][1] - 1]))
				elif item[1][0] == item[1][1]:
					array.append((item[0] + "(", [item[1][0]-1, item[1][1]]))
				elif item[1][0] == 0 and item[1][1] > 0:
					array.append((item[0] + ")", [item[1][0], item[1][1] - 1]))
				else:	
					print(item)
			retArray = array
		return [k[0] for k in retArray]    

obj = Solution()

print(obj.generateParenthesis(3))        

