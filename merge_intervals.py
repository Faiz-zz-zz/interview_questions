"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

"""
# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e




class Solution(object):
	def merge(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""
		
		if len(intervals) <= 1:
			return intervals
		
		retArray = []

		intervals.sort(key = lambda k: k.start)
		curr = intervals[0]
		for interval in (intervals):
			if curr.start <= interval.start and curr.end >= interval.start and curr.end <= interval.end:
				curr = Interval(curr.start, interval.end)
			elif curr.start <= interval.start and curr.end >= interval.end:
				curr = curr
			elif curr.start < interval.start and curr.end < interval.start:
				retArray.append(curr)
				curr = interval
		retArray.append(curr)		
		return retArray
			
		
ans = Solution().merge([Interval(1, 4), Interval(5, 6)])

for a in ans:
	print(a.start, a.end) 