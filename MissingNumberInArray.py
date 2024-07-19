# Find the Missing Number

# Given an array arr[] of size N-1 with integers in the range of [1, N], 
# the task is to find the missing number from the first N integers.

# Note: There are no duplicates in the list.

# Examples: 

# Input: arr[] = {1, 2, 4, 6, 3, 7, 8} , N = 8
# Output: 5
# Explanation: Here the size of the array is 8, so the range will be [1, 8]. 
# The missing number between 1 to 8 is 5

# Input: arr[] = {1, 2, 3, 5}, N = 5
# Output: 4
# Explanation: Here the size of the array is 4, so the range will be [1, 5]. 
# The missing number between 1 to 5 is 4

def FindNumber(arr, N):
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(arr)
    
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Test function
def Test_FindNumber():
    test_cases = [
        ([1, 2, 4, 6, 3, 7, 8], 8, 5),
        ([1, 2, 3, 5], 5, 4),
        ([1, 3, 4, 5], 5, 2),
        ([2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 10)
    ]
    
    for i, (arr, N, expected) in enumerate(test_cases):
        result = FindNumber(arr, N)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

Test_FindNumber()

