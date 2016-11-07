class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list()
        for i in range(0, len(nums)):
            nums[abs(nums[i])-1] *= -1
            if nums[abs(nums[i])-1] > 0:
                res.append(abs(nums[i]))
                print("Here")
            print(nums)
        return res
print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
