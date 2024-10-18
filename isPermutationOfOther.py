"""
Given two strings, write a method to decide if one is a permutation of the
other.

example:
    a = "infoosorr"
    b = "niooorrsf"
    return True
"""

def isPermutationOfOther(a, b):
    if len(a) != len(b):
        return False # can't be permutation
    counts = {}      # store the char count
    for char in a:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char in b:
        if char in counts:
            counts[char] -= 1
            if counts[char] == 0:
                del counts[char]
        else:
            return False
    return True

a = "ab"
b = "ba"
print(isPermutationOfOther(a, b))
