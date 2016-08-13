"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Hint:

Try two pointers.
Did you use the property of "the order of elements can be changed"?
What happens when the elements to remove are rare?

"""

class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		count = 0
		start = 0
		end = len(nums) - 1
		
		while start < len(nums):
			if nums[start] == val:
				while nums[end] == val and end >= 0:
					end -= 1
				nums[start] = nums[end]
				end -= 1
				count += 1
				start += 1
			else:
				start += 1
		return len(nums) - count                

obj = Solution()
array = [0,4,4,0,4,4,4,0,2]
print(obj.removeElement(array, 4), array)        

