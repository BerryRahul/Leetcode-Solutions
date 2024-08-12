
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # First Method
    # s = set(nums)
    # if len(s) != len(nums):
    #     return True
    # return False

    # Second Method
    s = set()
        
    for i in nums: 
        if i in s: 
            return True
        s.add(i)
    return False 