"""
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
this case, the max area of water (blue section) the container can contain is 49.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j, maxarea = 0, len(height)-1, 0 # initializing
        while j>i:
            area = (j - i) * min(height[i], height[j])  # calculate area
            maxarea = max(maxarea, area)                # select max of both
            if height[j] > height[i]:                   # shift the pointer
                i += 1                                  # which has lesser height
            else:                                       # as area is determined by that
                j -= 1
        return maxarea                                  # return the maxarea


if __name__ == '__main__':
    obj = Solution()
    arr= [1,8,6,2,5,4,8,3,7]
    print(obj.maxArea(arr))
