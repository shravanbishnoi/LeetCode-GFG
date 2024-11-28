"""
Dutch Flag Problem:
Given an array of integers, and a value x. Perform a 
inplace partition such that all the elements less than x
occurs before the elements that are greater than x.
"""
def DutchFlagProblem(lst, x):
    if len(lst) == 0:
        return "List is empty"

    low, current, high = 0, 0, len(lst) - 1

    while current <= high:
        if lst[current] < x:
            lst[low], lst[current] = lst[current], lst[low]
            low += 1
            current += 1
        elif lst[current] > x:
            lst[current], lst[high] = lst[high], lst[current]
            high -= 1
        else:
            current += 1

    return lst

lst = [2, 5, 11, 2, 4, 3, 7, 10, 8, 4, -4, 4]
print(DutchFlagProblem(lst=lst, x=5))
