"""
Given a set of candidate numbers (C) and a target number (T),
 find all unique combinations in C where the candidate numbers sums to T.

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

    def combinationSum1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        retArray = []
        def recurMethod(target, start, valuelist):
            length = len(candidates)
            print(valuelist)
            if target == 0:
                retArray.append(valuelist)
                return
            for i in range(start, length):
                if target < candidates[i]:
                    return
                recurMethod(target - candidates[i], i, valuelist + [candidates[i]])

        recurMethod(target, 0, [])

        return retArray

obj = Solution()

print(obj.combinationSum1([8, 7, 4, 3], 11))
