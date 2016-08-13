class Solution(object):
	def maxEnvelopes(self, envelopes):
		nums = sorted(envelopes, cmp = lambda x,y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
		length = len(nums)
		memo = []
		for x in range(length):
			low, high = 0, len(memo) - 1
			while low <= high:
				mid = (low + high) // 2
				if memo[mid][1] < nums[x][1]:
					low = mid + 1
				else:
					high = mid - 1
			if low < len(memo):
				memo[low] = nums[x]
			else:
				memo.append(nums[x])
		return len(memo)   