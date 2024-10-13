"""
Given two sorted arrays, find the number of elements in common.
The arrays are the same length and each has all distinct elements.

Example:
    A: 13, 27, 35, 40, 49, 55, 59
    B: 17, 35, 39, 40, 55, 58, 60
"""

def findCommonElements(a, b):
    commonElements = 0
    i = 0
    j = 0
    while (i < len(a) and j < len(b)):
        if (a[i] == b[j]):
            commonElements += 1
            i += 1
        elif (a[i] < b[j]):
            i += 1
        elif (a[i] > b[j]):
            j += 1
    return commonElements

a = [13, 27, 35, 40, 49, 55, 59]
b = [17, 35, 39, 40, 55, 58, 60]
print(findCommonElements(a, b))
