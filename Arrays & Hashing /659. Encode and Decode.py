def encode(strs: List[str]) -> str:
    """
    """
    res = ""
    for word in strs:
        res += str(len(word)) + "#" + word
    return res

def decode(s: str) -> List[str]:
    """
    """
    res, i = [], 0
    while i < len(s): 
        j = i 
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length 
        res.append(s[i:j])
        i = j 
    return res