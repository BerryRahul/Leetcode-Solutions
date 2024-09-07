from collections import defaultdict
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # if each string has the same amount of each letter when compared it is an anagram 
    # This solution is O(m*n) time where m is the amount of strings, and n is the average 
    # length of strings 
    result = defaultdict(list)
    for string in strs: 
        count = [0] * 6 
        for letter in string: 
            count[ord(letter) - ord("a")] += 1
        result[tuple(count)].append(string)
    return result.values()