from removeElement import Solution

s=Solution()


nums = [3,2,2,3]
val = 3
print(s.removeElement(nums,val),nums)


nums = [0,1,2,2,3,0,4,2]
val = 2
k=s.removeElement(nums,val)
print(k,nums)
