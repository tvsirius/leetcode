"""
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted."""
from removeDuplicates import Solution

s=Solution()

print("Test of leetcode\TopInterview150\80. Remove Duplicates from Sorted Array II")


nums = [1,1,2]
print("Test list is", nums)
k=s.removeDuplicates(nums)
print("List with removed dublicates is",nums,'Number of elements=',k,'\n\n')

nums = [0,0,1,1,1,2,2,3,3,4]
print("Test list is", nums)
k=s.removeDuplicates(nums)
print("List with removed dublicates is",nums,'Number of elements=',k,'\n\n')

nums = [0,0,0,1,1,1,2,2,2,3,3,4,5,7,8,11,11,11,11,11,15]
print("Test list is", nums)
k=s.removeDuplicates(nums)
print("List with removed dublicates is",nums,'Number of elements=',k,'\n\n')