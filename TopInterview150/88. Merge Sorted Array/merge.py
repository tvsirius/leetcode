"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """Merging two sorted lists inplace to first list

        Args:
            nums1 (list[int]): first list with len of two lists and m elements of its own, will be modified to hold the result
            m (int): nums1 elements count
            nums2 (list[int]): list with n elements to be merged with nums1
            n (int): nums2 elements count
            
        Do not return anything, modify nums1 in-place instead.
        """
        # i will loop using counters of two lists as a loop condition. I will fill the nums1 from the end with the biggest element of this two lists (looking in the m and n indexes), 
        # and decrease corresponding index. 
        
        # position to write element, decreasing, starting from the end of nums1        
        counter = m + n
        
        #  loop condition is while both nums1 and nums2 have elements
        while m > 0 and n > 0:
            # decreasing counter in any case
            counter -= 1
            
            # nums1 have space reserved in the end, so it's original elements will be safe

            if nums1[m - 1] > nums2[n - 1]:
                m -= 1
                nums1[counter] = nums1[m]
            else:
                n -= 1
                nums1[counter] = nums2[n]

        # we dont care if m>0, because if nums1 have m elements left they are already in place!
        if n>0:
            nums1[:counter]=nums2[:counter]