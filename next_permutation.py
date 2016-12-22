"""
 QuestionEditorial Solution  My Submissions
Total Accepted: 73504
Total Submissions: 270646
Difficulty: Medium
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		if len(nums) < 2:
			return

		back = 0
		start = 0

		for i in reversed(range(len(nums) - 1)):
			if nums[i] < nums[i+1]:
				back = i
				break

		for i in reversed(range(back, len(nums))):
			if nums[i] > nums[back]:
				start = i
				break
		nums[start], nums[back] = nums[back], nums[start]
		if start == 0 and back == 0:
			nums.reverse()
		else:
			nums[back + 1:] = reversed(nums[back + 1:])


		# print(nums)



obj = Solution()
array = [3, 2, 1]
obj.nextPermutation(array)
print(array)
