"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(str(''.join(map(str, digits))))
        num += 1
        return list(map(int, list(str(num))))
        
print(Solution().plusOne([9,9,9]))