"""
You are given with a non empty, non-null case sensitive string of alphanumeric character
Return True if it contains duplicate character otherwise False.

Example: 
    s = "abcd" --> False
    s = "abccd" --> True
    s = "aaaa" --> True
    s = "AabcsejkdS" --> False

"""

def containsDuplicate(s):
    if s == "" or s == None:
        return False
    charsPresent = set()
    for char in s:
        if char in charsPresent:
            return True
        else:
            charsPresent.add(char)
    return False

strings = ["aaaa", "Aabhksd", "abcd", "", None, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789bksugnero"]
for s in strings:
    print(f"{s}--->", containsDuplicate(s))
