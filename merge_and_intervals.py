"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.

"""

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
    	array = []
    	for interval in intervals:
    		if new_interval.start > intervals.end:
    			array.append(interval)
    		elif interval.start > new_interval.end:
    			array.append(new_interval)
    			new_interval = interval
    		else:
    			newInterval.end = max(interval.end, new_interval.end)
    			new_interval.start = min(interval.start, new_interval.start)
    	array.append(new_interval)
    	return array		



    	