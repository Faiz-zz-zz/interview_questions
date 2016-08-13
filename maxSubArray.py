class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        if len(list(filter(lambda x: x >=0, A))) == 0:
            return
        currSum = 0
        maxSum = 0
        returnStart, returnEnd = 0, 0
        start, end = 0, 0
        newStart = False
        wasInNeg = False
        for i in range(len(A)):
            if newStart and A[i] > 0:
                wasInNeg = False
                end = start = i
                newStart = False
            if A[i] > 0:
                currSum += A[i]
                end = i
            else:
                if not wasInNeg:
                    newStart = True
                    wasInNeg = True
                    if currSum == maxSum:
                        returnStart, returnEnd = max(((returnStart, returnEnd),(start, end)), key = lambda k: k[1] - k[0])
                    elif currSum > maxSum:
                        maxSum = currSum
                        returnStart, returnEnd = start, end
        return A[returnStart:returnEnd+1]            
                        
                                           
                        
obj = Solution()

print(obj.maxset([-1, -1, -1, -1]))        