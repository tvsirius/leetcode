"""
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.
"""
from removeElement import Solution

s=Solution()

print("Test of leetcode\TopInterview150\27. Remove Element")

nums = [3,2,2,3]
val = 3
print(f"Testing with nums={nums}, val={val}")
unique_elements=s.removeElement(nums,val)
print(f"Processed nums=",nums,'unique elements=',unique_elements,'\n\n')


nums = [0,1,2,2,3,0,4,2]
val = 2
print(f"Testing with nums={nums}, val={val}")
unique_elements=s.removeElement(nums,val)
print(f"Processed nums=",nums,'unique elements=',unique_elements,'\n\n')
