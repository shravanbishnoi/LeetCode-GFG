"""
Q1. Given a list of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice and the target will not be present in the array.
If there is no solution then return empty list?
"""
def twoNumTarget(lst, target):
    seen = {}
    result = []
    for i in range(len(lst)):
        complement = target - lst[i]

        if complement in seen:
            result.append((seen[complement], i))
        seen[complement] = i
    return result

print(twoNumTarget([1,2,3,4,4], 8))
