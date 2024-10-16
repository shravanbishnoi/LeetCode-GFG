"""
There are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
Example:
    pale, ple -> true
    pales, pale -> true
    pale, bale -> true
    pale, bake -> false

"""

def editDistance(s, l):
    editCount = 0
    if len(s) == len(l):
        for i in range(len(s)):
            if s[i] != l[i]:
                editCount += 1
        return editCount < 2
    elif (len(s) > len(l)):
        s, l = l, s
    j = 0
    for i in range(len(l)):
        if j >= len(s) or s[j] != l[i]:
            editCount += 1
        else:
            j += 1
    return editCount < 2

s = "pales"
l = "pale"
print(editDistance(s, l))
