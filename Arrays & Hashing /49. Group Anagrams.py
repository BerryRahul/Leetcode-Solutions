from collections import defaultdict
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # if each string has the same amount of each letter when compared it is an anagram 
    # This solution is O(m*n) time where m is the length of strs, and n is the average 
    # length of strings 
    result = defaultdict(list)
    for s in strs: 
        count = [0] * 26 # all letters 
        for c in s: 
            count[ord(c) - ord("a")] += 1
        result[tuple(count)].append(s)
    return result.values


