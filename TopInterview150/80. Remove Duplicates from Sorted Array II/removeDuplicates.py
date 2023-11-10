"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # I am looping through the list and on each iteration I either move element (so all valid elements is moved in order from the start of list),
        # either skip in given valid-non-valid condition (max of 2 occurrences)
        # I will need to keep m3 m2 m1 variables with the copy of unmodified list [i-2][i-1][i], which will be not affected by moving process
        # so if [i-2] is less then [i] then [i] element is valid. ( 0 0 1 1 2 2 2* 3 ) - on marked 2*   element [i-2]=[i]=2 and this will be condition to increase offset, 
        # and on next i, [i-2]=2 and [i]=3, so 3 will be moved to place of 2*
        
        offset=0 # no duplicate in the start

        m2=nums[0]
        m1=nums[1] if len(nums)>1 else m2 # to make it work with 1 element list
        for i in range(2,len(nums)):
            # keeping our unmodified copy of 3 last elements  
            m3=m2
            m2=m1
            m1=nums[i]
            if m1>m3:
                nums[i-offset]=nums[i]
            else:
                offset+=1
        # offset = number of unvalid elements
        return len(nums)-offset