"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, \
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything \
from your function.

Author: Juliet George
Date: 8/24/2020

"""
class Solution(object):
    def duplicateZeros(self, arr):
        """
        No return - modify array in place.

        Examples:
        Example 1:

        Input: [1,0,2,3,0,4,5,0]
        Output: null
        Explanation: After calling your function, the input array is modified \
         to: [1,0,0,2,3,0,0,4]
        Example 2:

        Input: [1,2,3]
        Output: null
        Explanation: After calling your function, the input array is modified \
        to: [1,2,3]
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        init_length = len(arr)
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i+1,0)
                i = i+2
            else:
                i = i+1
        while len(arr) > init_length:
            arr.pop()
