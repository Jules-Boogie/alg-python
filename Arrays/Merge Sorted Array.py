"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as \
 one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to \
 hold additional elements from nums2.

Author: Juliet George
Date: 8/24/2020
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        No return - modify nums1 in place.

        Examples:
        Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

        Output: [1,2,2,3,5,6]
        
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) > m:
            nums1.pop()
        nums1.extend(nums2)
        return nums1.sort()
