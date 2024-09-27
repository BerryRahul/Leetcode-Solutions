def repeatedCharacter(s):
    """
    :type s: str
    :rtype: str
    """
    tracker = []
    for i in s: 
        if i in tracker: 
            return i
        else: 
            tracker.append(i)
