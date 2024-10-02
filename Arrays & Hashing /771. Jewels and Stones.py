def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    c = 0
    for i in set(jewels):
        c += stones.count(i)
    return c
