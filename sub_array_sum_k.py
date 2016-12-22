"""
subarray sum k
"""

def subarray_sum(array, k):
    curr_sum = array[0]
    start = 0

    for i in range(1, len(array) + 1):
        while curr_sum > k and start < i - 1:
            curr_sum = curr_sum - array[start]
            start += 1

        if curr_sum == k:
            return array[start: i]

        if i < len(array):
            curr_sum = curr_sum + array[i]

    return []

print(subarray_sum([1, 2, 3, 4], 6))
