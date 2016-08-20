"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.


Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 2, 3, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]

"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        retArray = [] 
        def recurMethod(array_so_far, candidates):
            if sum(array_so_far) == target:
                retArray.append(array_so_far)
                
            if len(candidates) == 0:
                return 
                
            if not sum(array_so_far + [candidates[0]]) > target:
                recurMethod(array_so_far + [candidates[0]], candidates[1:])
                recurMethod(array_so_far, candidates[1:])
                
        recurMethod([], candidates) 

        return retArray   
            
obj = Solution()

print(obj.combinationSum([2, 2, 3, 7], 7))            