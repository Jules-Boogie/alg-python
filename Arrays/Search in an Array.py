"""
Given an array arr of integers, check if there exists two integers \n
N and M such that N is the double of M ( i.e. N = 2 * M).

Author: Juliet George
Date: 9/5/2020
"""

class Solution(object):
    def checkIfExist(self, arr):
        """
        Returns true if an element and its double is in the area
        :type arr: List[int]
        :rtype: bool
        """

        if arr.count(0) >= 2:
            return True

        for el in arr:
            double = el + el
            if double in arr and arr.index(double) != arr.index(el):
                return True
        return False
