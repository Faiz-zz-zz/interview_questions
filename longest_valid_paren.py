class Solution(object):
    def longestValidParentheses(self, s):
        maxLen = 0
        stack = []
        last = -1
        for i in range(len(s)):
	        if s[i] == '(':
                stack.append(i)
            else:
				if stack == []:
					last = i
				else:
					stack.pop()
					if stack == []:
						maxLen = max(maxLen, i - last)
					else:
						maxLen = max(maxLen, i - stack[len(stack) - 1])
            print(stack)
		return maxLen

print(Solution().longestValidParentheses("(((())))"))

# def dutch(array, a, b):
#      i, k, j = 0, 0, len(array) - 1
#      while k <= j:
#          if array[k] < a:
#              array[i], array[k] = array[k], array[i]
#              i += 1
#          elif array[k] > b:
#              array[j], array[k] = array[k], array[j]
#              j -= 1
#          k += 1
#      return array
