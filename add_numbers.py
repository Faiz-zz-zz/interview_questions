"""
Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.

"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1 = "0"*(len(num2) - len(num1)) + num1
        else:
            num2 = "0"*(len(num1) - len(num2)) + num2
        answer = ""

        carry = 0

        for i in range(len(num1) - 1, -1, -1):
            res = str(int(num1[i]) + int(num2[i]) + carry)
            if len(str(res)) > 1:
                carry = int(res[0])
                res = res[1:]
            else:
                carry = 0
            answer = res + answer
        answer = str(carry) + answer

        return str(int(answer))

print(Solution().addStrings("100000000", "99"))
