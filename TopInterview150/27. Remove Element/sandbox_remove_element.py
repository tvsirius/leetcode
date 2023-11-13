from remove_element import removeElement

print("Test of leetcode/TopInterview150/27. Remove Element \n")

nums = [3,2,2,3]
val = 3
print(f"Testing with nums={nums}, val={val}")
unique_elements=removeElement(nums,val)
print(f"Processed nums=",nums,'unique elements=',unique_elements,'\n\n')


nums = [0,1,2,2,3,0,4,2]
val = 2
print(f"Testing with nums={nums}, val={val}")
unique_elements=removeElement(nums,val)
print(f"Processed nums=",nums,'unique elements=',unique_elements,'\n\n')
