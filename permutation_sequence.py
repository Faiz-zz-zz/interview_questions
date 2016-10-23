"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorials = [1 for i in range(n + 1)]

        for i in range(1, len(factorials)):
            factorials[i] = i * factorials[i - 1]

        answer = [i for i in range(1, n + 1)]
        result = ""
        for i in range(n, 0, -1):
            ind = (k - 1)//(factorials[i - 1])
            result += str(answer[ind])
            del answer[ind]
            k %= factorials[i - 1]
        return result

print(Solution().getPermutation(4, 14))
