# Courera Question

def solution(steps):
    currRect = steps[0]
    for step in steps[1:]:
        top = min(step[1], currRect[1])
        right = min(step[0], currRect[0])
        currRect = (right, top)
    print((currRect[0]) * (currRect[1]))
