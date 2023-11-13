from remove_duplicates import removeDuplicates

print("Test of leetcod/TopInterview150/26. Remove Duplicates from Sorted Array\n")


nums = [1,1,2]
print("Test list is", nums)
k=removeDuplicates(nums)
print("List with removed duplicates is",nums,'Number of elements=',k,'\n\n')

nums = [0,0,1,1,1,2,2,3,3,4]
print("Test list is", nums)
k=removeDuplicates(nums)
print("List with removed duplicates is",nums,'Number of elements=',k,'\n\n')

nums = [0,0,0,1,1,1,2,2,2,3,3,4,5,7,8,11,11,11,11,11,15]
print("Test list is", nums)
k=removeDuplicates(nums)
print("List with removed duplicates is",nums,'Number of elements=',k,'\n\n')