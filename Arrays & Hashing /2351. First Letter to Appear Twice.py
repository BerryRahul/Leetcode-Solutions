def repeatedCharacter(s):
    """
    :type s: str
    :rtype: str
    """
    # A hashset is not necessary given the initial conditions 
    # also because we are only keeping track of lowercase letters 
    tracker = []
    for i in s: 
        if i in tracker: 
            return i
        else: 
            tracker.append(i)
