"""
Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
"""

def displayMatrix(m):
    for i in m:
        for j in i:
            print(j, end=" ")
        print()

def zeroMatrix(matrix):
    trackZeros = {}
    for i in range(1-len(matrix[0]), len(matrix)):
        trackZeros[i] = False

    print(trackZeros)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                trackZeros[i] = True
                trackZeros[-(j-1)] = False

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if trackZeros[i] or trackZeros[-(j-1)]:
                matrix[i][j] = 0
    return matrix

matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
displayMatrix(matrix)
new = zeroMatrix(matrix)
displayMatrix(new)
