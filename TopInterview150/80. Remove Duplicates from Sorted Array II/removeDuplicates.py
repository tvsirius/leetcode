"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        offset=0
        m2=nums[0]
        m1=nums[1] if len(nums)>1 else m2
        for i in range(2,len(nums)):
            m3=m2
            m2=m1
            m1=nums[i]
            if m1>m3:
                nums[i-offset]=nums[i]
            else:
                offset+=1
        return len(nums)-offset