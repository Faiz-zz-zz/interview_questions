def answer1(heights):
	total = 0
	for lev in range(max(heights), 0, -1):
		level = [-1 if x >= lev else 0 for x in heights]
		seenAWall = False
		for hutch in range(len(level)):
			if level[hutch] == -1:
				seenAWall = True
			if level[hutch] != -1:
				if seenAWall:
					level[hutch] += 1

		seenAWall = False			
		for hutch in reversed(range(len(level))):
			if level[hutch] == -1:
				seenAWall = True
			if level[hutch] != -1:
				if seenAWall:
					level[hutch] += 1

		total += level.count(2)

	return total

def answer(heights):
	total = 0
	position = 0
	currHeight = heights[position]
	maxSoFar = maxInTheFront = heights[position]
	for height in heights[:-1]:
	    maxSoFar = max(maxSoFar, height)
	    maxInTheFront = max(heights[position:])
	    total += min(maxSoFar, maxInTheFront) - height
	    position += 1
	return total    



print(answer([1, 4, 2, 5, 1, 2, 3]))		


