"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])


"""

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        array = [0, 10]
        for i in range(2, n+1):
            number = 9
            for h in range(9 - i + 2, 10):
                number = number*h
            array.append(array[-1] + number)
        print array    
        return array[-1]    