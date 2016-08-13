"""
Bus drivers in an Andean city gossip alot! They only gossip when their routes intersect, and they are at the same stop. The problem is as follows: If each driver starts with one piece of gossip, how long does it take till all the drivers know all the gossips?

Input will be in the form of bus routes, each route will be on a different line like so:

1 3 5 6
3 4 2 1
1 4 3
This shows 3 bus routes, as you can see not all routes are of the same length.

Gossip happens when two (or more) drivers are at the same stop, even if its the start. It takes a minute to go from stop to stop, and gossip exchange is instant. Routes repeat, so if a drivers route is 1 2 3 then he will follow 1 2 3 1 2 3 1 2 3 ... for the entire day. A day is 8 hours for all our drivers so the maximum amount of time to get all the gossip around is 480 minutes.

Output should be a single number, which is the number of minutes needed for gossip to be distributed. If all the drivers do not receive the gossip by the end, print 'never'.

Example Input

3 1 2 3
3 2 3 1 
4 2 3 4 5
Example Output

 5
"""

# drivers = 3

# route = []

# for i in range(drivers):
# 	route.append(list(map(int, input().split())))

# gossip = []
# for i in range(len(route)):
# 	gossip.append([0 for i in range(len(route))])
# 	gossip[i][i] = 1

# minute = 0
# index = 0

# mile = len(gossip) ** 2

# while minute < 480 and sum(map(sum, gossip)) != mile:
# 	stop = []
# 	for i in range(drivers):
# 		stop.append(route[i][index % len(route[i])])

	
# 

validate = []

def check(validate = validate):
	return sum(list(map(len, validate))) == 9		

zero = list(map(int, input().split()))
one = list(map(int, input().split()))
two = list(map(int, input().split()))

for i in range(480):
	print(zero[i % len(zero)], one[i % len(one)], two[i % len(two)])

for i in range(3):
	validate.append(set([i]))

minute = 0
index = 0
while minute < 480 and not check():
	print(validate)
	if zero[index % len(zero)] == one[index % len(one)]:
		validate[0].add(1)
		validate[1].add(0)
	elif zero[index % len(zero)] == two[index % len(two)]:
		validate[0].add(2)
		validate[2].add(0)
	elif one[index % len(one)] == two[index % len(two)]:
		validate[1].add(2)
		validate[2].add(1)

	index += 1
	minute += 1

if minute != 480:
	print(index - 1)
else:
	print("never")			
				




























