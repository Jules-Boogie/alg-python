"""
Given an array of integers A sorted in non-decreasing order, return an array \
of the squares of each number, also in sorted non-decreasing order.

Author: Juliet George
Date: 8/24/2020
"""

class Solution(object):
    def sortedSquares(self, A):
        """
        Returns the a new list with squares of the elements the old \
        list in ascending order.

        Examples:
        Example 1:

        Input: [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        Example 2:

        Input: [-7,-3,2,3,11]
        Output: [4,9,9,49,121]

        :type A: List[int]
        :rtype: List[int]
        """
        arr = [(val * val) for val in A]
        return sorted(arr,reverse=False)
