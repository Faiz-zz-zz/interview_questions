"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

"""

def isBadVersion(num):
	dictions = {1:False, 2:True}
	return dictions[num]


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
        	return 1

        left = 0
        right = n - 1
        mid = (left + right) // 2

        while left <= right:
        	if isBadVersion(mid + 1) and isBadVersion(mid) == False:
        		return mid + 1
        	elif isBadVersion(mid + 1):
        		right = mid - 1
        	else:
        		left = mid + 1	
        	mid = (left + right) // 2	

obj = Solution()
print(obj.firstBadVersion(2))        		