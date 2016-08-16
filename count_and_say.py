"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""
from itertools import groupby

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = "1"
        for i in range(int(n)):
        	print()
        	new = ""
        	for k, g in groupby(string):
        		new += str(len(list(g))) + k
        		print(new)
        	string = new
        return string		


obj = Solution()
print(obj.countAndSay("1"))