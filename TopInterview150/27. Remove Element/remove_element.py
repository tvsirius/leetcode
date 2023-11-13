def removeElement(nums: list[int], val: int) -> int:
    """Removes all val occurrences from list nums

    Args:
        nums (list[int]): list to process
        val (int): element to remove

    Returns:
        int: k - number of valid (non equal to val) elements
    """
    # processing in place require moving all elements except val in the beginning of the list
    # i will loop thought with offset, counting number of VAL found so far, 
    # giving me the idea of where to move next valid element 
    offset=0 # no VAL found yet
    for i in range(len(nums)):
        if nums[i]==val:
            # no moving, but increase offset
            offset+=1
        else:
            # make a move (VAL occurrences will be overwritten)
            nums[i-offset]=nums[i]
    # k is obvious 
    return len(nums)-offset

