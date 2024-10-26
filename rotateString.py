"""
Assume that you have a method isSubtring which checks if one word is a substringof another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g, "waterbottle" is a rotation of "erbottlewat").
"""

def isSubstring(string, substring):
    if len(substring) == 0:
        return True
    elif len(string) < len(substring):
        return False
    idx = 0
    for i in range(len(string)):
        if string[i] == substring[idx]:
            idx += 1
            if len(substring) == idx:
                return True
        elif (string[i] == substring[0]):
            idx = 1
        else:
            idx = 0
    return False

def rotateString(s1, s2):
    """Returns True, if s2 is a rotation of s1"""
    if len(s1) != len(s2):
        return False
    return isSubstring(s1 + s1, s2)

s1 = "waterbottle"
s2 = "erbottlewat"
print(rotateString(s1, s2))

