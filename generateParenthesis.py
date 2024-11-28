"""
22. Generate Parentheses
Medium
Topics
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(cur, open, close):
            if len(cur) == 2*n:
                result.append("".join(cur))
                return
            if open < n:
                cur.append('(')
                backtrack(cur, open+1, close)
                cur.pop()
            if close < open:
                cur.append(')')
                backtrack(cur, open, close+1)
                cur.pop()
        result = []
        backtrack([], 0, 0)
        return result
        