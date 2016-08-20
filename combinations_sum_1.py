"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
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
            	array_so_far.sort()
            	if array_so_far not in retArray:
                	retArray.append(array_so_far)
                
            for i in candidates:      
                if not sum(array_so_far + [i]) > target:
                    recurMethod(array_so_far + [i], candidates)
                
        recurMethod([], candidates) 

        return retArray

obj = Solution()

print(obj.combinationSum([92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73], 310))