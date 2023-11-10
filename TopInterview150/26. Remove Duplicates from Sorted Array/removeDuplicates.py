"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """Remove duplicates from sorted list in place and return numbers of unique elements

        Args:
            nums (list[int]): List to process

        Raises:
            AssertionError: if list is not sorted!

        Returns:
            int: Unique elements in nums count
        """
        # I am looping through the list and on each iteration I either move element (so all unique elements is moved in order from the start of list),
        # either skip and increase offset, which tells me how many duplicate i have found so far
        
        offset=0 # no duplicate in the start
        
        for i in range(1,len(nums)):
            # if element at i it is equal to i-1 then it is a duplicate
            if nums[i]>nums[i-1]:
                # we have analyzed and saved all elements before i, so it is safe to write to i-offset 
                nums[i-offset]=nums[i]
                
            elif nums[i]==nums[i-1]:
                # this element will be overwritten 
                offset+=1
                
            else: #special check, may be not needed! 
                raise AssertionError("Nums not sorted!")
        # offset is a count of found duplicates
        return len(nums)-offset
