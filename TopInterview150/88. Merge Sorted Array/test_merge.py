from merge import Solution
s=Solution()

print("Test of leetcode\TopInterview150\88. Merge Sorted Array ")

nums1 = [1,2,3,7,100,0,0,0,0,0,0,0]
m = 5
nums2 = [-12,1,4,5,15,20,62]
n = 7
s.merge(nums1,m,nums2,n)

print(nums1)


nums1 = [0]
m = 0
nums2 = [1]
n = 1
s.merge(nums1,m,nums2,n)
print(nums1)

