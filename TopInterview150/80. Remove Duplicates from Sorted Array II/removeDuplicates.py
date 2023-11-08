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