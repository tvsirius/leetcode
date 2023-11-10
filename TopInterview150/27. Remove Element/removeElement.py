"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # processing in place require moving all elements except val in the beginning of the list
        # i will loop thought with offset, counting number of VAL found so far, 
        # giving me the idea of where to move next valid element 
        offset=0 # no VAL found yet
        for i in range(len(nums)):
            if nums[i]==val:
                # no moving, but increase offset
                offset+=1
            else:
                # make a move (VAL occurrences will be overwritten)
                nums[i-offset]=nums[i]
        # k is obvious 
        return len(nums)-offset

