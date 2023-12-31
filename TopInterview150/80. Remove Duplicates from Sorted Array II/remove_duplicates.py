def removeDuplicates(nums: list[int]) -> int:
    """Remove double duplicates (valid elements may appear at maximum two times) from sorted list in place and return numbers of valid elements

    Args:
        nums (list[int]): List to process

    Returns:
        int: Valid elements (with appear at max two times) in nums count
    """
    # I am looping through the list and on each iteration I either move element (so all valid elements is moved in order from the start of list),
    # either skip in given valid-non-valid condition (max of 2 occurrences)
    # I will need to keep m3 m2 m1 variables with the copy of unmodified list [i-2][i-1][i], which will be not affected by moving process
    # so if [i-2] is less then [i] then [i] element is valid. ( 0 0 1 1 2 2 2* 3 ) - on marked 2*   element [i-2]=[i]=2 and this will be condition to increase offset, 
    # and on next i, [i-2]=2 and [i]=3, so 3 will be moved to place of 2*
    
    offset=0 # no duplicate in the start

    m2=nums[0]
    m1=nums[1] if len(nums)>1 else m2 # to make it work with 1 element list
    for i in range(2,len(nums)):
        # keeping our unmodified copy of 3 last elements  
        m3=m2
        m2=m1
        m1=nums[i]
        if m1>m3:
            nums[i-offset]=nums[i]
        else:
            offset+=1
    # offset = number of invalid elements
    return len(nums)-offset