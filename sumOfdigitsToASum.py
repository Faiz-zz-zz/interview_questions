def sumOfDigitsToASum(summation, numOfDigits):

	if numOfDigits == 0:
		return 0

	ans = 0	

	for i in range(10):
		if summation - i >= 0:
			ans += sumOfDigitsToASum(summation - i, numOfDigits - 1)

	return ans 


ans = 0

for i in range(10):
	ans += sumOfDigitsToASum(10 - i, 2 - 1)

print(ans)	