"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.


"""


class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
			
		if len(nums) == 1:
			return nums
		elif len(nums) == 0:
			return []   


		start = 1
		end = start
		prev = nums[start]
		
		while end < len(nums):
			while nums[end] == prev and end < len():
				end += 1
			prev = nums[end]
			nums[start] = nums[end]
			start += 1

		return 	
	

obj = Solution()
array = [1,1,2]
print(obj.removeDuplicates(array), array)