from merge import merge

print("Test of leetcode/TopInterview150/88. Merge Sorted Array \n")

nums1 = [1,2,3,7,100,0,0,0,0,0,0,0]
m = 5
nums2 = [-12,1,4,5,15,20,62]
n = 7
print(f"Test lists is nums1={nums1} ,m={m}, nums2={nums2}, n={n}")
merge(nums1,m,nums2,n)
print(f"Merged list={nums1}\n\n")


nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(f"Test lists is nums1={nums1} ,m={m}, nums2={nums2}, n={n}")
merge(nums1,m,nums2,n)
print(f"Merged list={nums1}\n\n")


nums1 = [1,0,0,0,0,0,0,0]
m = 1
nums2 = [-12,1,4,5,15,20,62]
n = 7
print(f"Test lists is nums1={nums1} ,m={m}, nums2={nums2}, n={n}")
merge(nums1,m,nums2,n)
print(f"Merged list={nums1}\n\n")
