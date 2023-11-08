class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        offset=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                nums[i-offset]=nums[i]
            elif nums[i]==nums[i-1]:
                offset+=1
            else:
                raise AssertionError("Nums not sorted!")
        return len(nums)-offset
