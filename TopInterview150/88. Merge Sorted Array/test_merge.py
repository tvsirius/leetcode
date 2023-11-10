"""Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 
"""

from merge import Solution
s=Solution()

print("Test of leetcode/TopInterview150/88. Merge Sorted Array \n")

nums1 = [1,2,3,7,100,0,0,0,0,0,0,0]
m = 5
nums2 = [-12,1,4,5,15,20,62]
n = 7
print(f"Test lists is nums1={nums1} ,m={m}, nums2={nums2}, n={n}")
s.merge(nums1,m,nums2,n)
print(f"Merged list={nums1}\n\n")


nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(f"Test lists is nums1={nums1} ,m={m}, nums2={nums2}, n={n}")
s.merge(nums1,m,nums2,n)
print(f"Merged list={nums1}\n\n")


nums1 = [1,0,0,0,0,0,0,0]
m = 1
nums2 = [-12,1,4,5,15,20,62]
n = 7
print(f"Test lists is nums1={nums1} ,m={m}, nums2={nums2}, n={n}")
s.merge(nums1,m,nums2,n)
print(f"Merged list={nums1}\n\n")
