"""
 Isomorphic Strings
Solved
Easy
Topics
Companies
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true


"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        Scounts = {}
        Tcounts = {}
        
        for char_s, char_t in zip(s, t):
            if char_s in Scounts:
                if Scounts[char_s] != char_t:
                    return False
            else:
                Scounts[char_s] = char_t
            
            if char_t in Tcounts:
                if Tcounts[char_t] != char_s:
                    return False
            else:
                Tcounts[char_t] = char_s
                
        return True
