"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        array = []
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            print(start, end)
            while start < end:
                if nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                elif nums[i] + nums[start] + nums[end] < 0:
                    start -= 1
                else:
                    insert = [nums[i], nums[start], nums[end]]
                    if insert not in array:
                        array.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
        return array            
        


obj = Solution()

print(obj.threeSum([0,1,1]))        