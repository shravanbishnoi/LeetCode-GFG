"""
383. Ransom Note
Solved
Easy
Topics
Companies
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = {}
        for char in magazine:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        result = ""
        for char in ransomNote:
            if char in counts and counts[char] >= 1:
                result += char
                counts[char] -= 1
                if counts[char] == 0:
                    del counts[char]
            else:
                continue
        return result == ransomNote
        