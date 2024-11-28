"""
1.4:Palindrome permutation
Given a string, write a function to check if it is a permutation of a
palindrome. A permutation is a rearrangement of letters. The palindrome
does not need to be limited to just dictionary words.

Example:
Input: Tact Coa
Output: True ("taco cat", "atco cta" etc.)
"""

def palindromePermutation(string):
    if len(string) == 0:
        return "String is empty"
    string = string.lower()
    charCount = {}
    for char in string:
        if char != " ":
            if char in charCount:
                charCount[char] += 1
            else:
                charCount[char] = 1
    countOdds = 0
    for key,value in charCount.items():
        if value % 2 != 0:
            countOdds += 1
    return countOdds < 2

string = "Tact Coa"
print(palindromePermutation(string=string))
        