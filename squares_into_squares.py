"""
Given a positive integral number n, return a strictly increasing sequence
 (list/array/string depending on the language) of numbers,
  so that the sum of the squares is equal to n².

If there are multiple solutions (and there will be), return the result with
 the largest possible values:

Examples

decompose(11) must return [1,2,4,10]. Note that there are actually two ways
 to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but
  don't return [2,6,9], since 9 is smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since
 [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.

Note

Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists,
 return nil, null, Nothing, None (depending on the language) or "" (Java, C#)
  or {} (C++).
"""


def decompose(n):
    # your code
    array = []
    def recurMethod(n, sub_ans):
        square_sum = sum(map(lambda k: k**2, sub_ans))
        if square_sum > n**2:
            return
        if square_sum == n**2:
            if sorted(sub_ans) not in array:
                array.append(sorted(sub_ans))
        else:
            for i in range(1, n):
                if i not in sub_ans:
                    recurMethod(n, sub_ans + [i])
    for i in range(1, n):
        recurMethod(n, [i])
    print(array)

decompose(50)
