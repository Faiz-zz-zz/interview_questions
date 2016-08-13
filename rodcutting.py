def rodCutting(cost, length):
	price = 0
	if (length <= 0):
		return 0
	else:
		for i in range(1, length + 1):
			price = max(price, cost[i] + rodCutting(cost, length - i))
	return price

cost = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}	
print rodCutting(cost, 9)		