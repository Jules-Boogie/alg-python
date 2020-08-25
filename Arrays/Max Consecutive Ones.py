"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Author: Juliet George
Date: 8/24/2020
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        Returns the max occurrence of 1.
        Examples:
        Input: [1,1,0,1,1,1]
        Output: 3
        Explanation: The first two digits or the last three digits are \
        consecutive 1s.
        The maximum number of consecutive 1s is 3.
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max = 0
        for val in nums:
            if val == 1:
                count = count + 1
                if count > max:
                    max = count
            elif val == 0:
                count = 0
        return max
