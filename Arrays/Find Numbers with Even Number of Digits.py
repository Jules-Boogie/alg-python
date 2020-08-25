"""
Given an array nums of integers, return how many of them contain an even number of digits.

Author: Juliet George
Date: 8/24/2020
"""

class Solution(object):
    def findNumbers(self, nums):
        """
        Returns the number of items in the list that have even numbers of digits.

        Examples:
        Input: nums = [555,901,482,1771]
        Output: 1
        Explanation:
        Only 1771 contains an even number of digits.
        :type nums: List[int]
        :rtype: int
        """
        count1 = 0
        for val in nums:
            if len(str(val)) % 2 == 0:
                count1 = count1 + 1
        return count1
