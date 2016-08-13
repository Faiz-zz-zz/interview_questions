def answer(minions):
    # your code here
    solution = [((t / (n/d)), i) for i, (t, n, d) in enumerate(minions)]
    solution.sort(key = lambda k: k[0])
    return [x[1] for x in solution]

print(answer([[5, 1, 5], [10, 1, 2]]))    



# def answer(minions):
#     minion = [time / (numerator / denominator) for time, numerator, denominator in minions]
#     abstract = lambda x: minion[x]
#     return sorted(range(len(minions)), key=get_expect)

def answer(minions):
    # your code here
    solution = []
    for i, (t, n, d) in enumerate(minions):
        if n == 0:
            solution.append((t*100000000, i))
        elif d == 0:
            solution.append((t*0.000000000001, i))
        else:
            solution.append((t/(n/d), i))
    solution.sort(key = lambda k: k[0])
    return [x[1] for x in solution]

print(answer([[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]])) 