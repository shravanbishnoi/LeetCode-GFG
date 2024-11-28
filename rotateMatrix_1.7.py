"""
1.7: Rotate matrix
Given an image representation by an NxN matrix,
where each pixel in the image is 4bytes, write 
a method to rotate the image by 90 degrees, can you do this
in place?
"""
def rotateMatrix(matrix):
    k = len(matrix)
    for i in range(k // 2):
        for j in range(i, k - i - 1):
            top = matrix[i][j]
            right = matrix[j][k-1-i]
            bottom = matrix[k-1-i][k-1-j]
            left = matrix[k-1-j][i]

            matrix[i][j] = left
            matrix[j][k-1-i] = top
            matrix[k-1-i][k-1-j] = right
            matrix[k-1-j][i] = bottom
    return matrix


def display(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()

matrix = [
    [(1), (2), (3), (4)],
    [(5), (6), (7), (8)],
    [(9), (10), (11), (12)],
    [(13), (14), (15), (16)]
]
print(rotateMatrix(matrix=matrix))