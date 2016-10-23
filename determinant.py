"""
Write a function that accepts a square matrix (n x n 2D array) and returns the
determinant of the matrix.
"""


def determinant(matrix):
    def recurMethod(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        total = 0
        for ind, mult in enumerate(matrix[0]):
            new_matrix = []
            # create sub_matrix
            for row in matrix[1:]:
                sub_row = []
                for sub_ind, col in enumerate(row):
                    if sub_ind != ind:
                        sub_row.append(col)
                new_matrix.append(sub_row)
            if ind % 2 == 0:
                total += mult * recurMethod(new_matrix)
            else:
                total -= mult * recurMethod(new_matrix)
        return total
    return recurMethod(matrix)
print(determinant([[1, 1, 2], [2, 3, 4], [3, 4, 5]]))
