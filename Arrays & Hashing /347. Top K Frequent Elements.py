def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # this solution is O(n) + O(n) = O(n) time and memory 
    # A variation of bucket sort and heapify 
    # create an array subarrays with the length of nums 
    # count the frequency of each element in nums into a hashmap
    # then append the value into the index of the frequency array which indicates how many times any element oocurs 
    # then itterate through that array backwards appending to the final result array up until you have k items
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums: 
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items(): 
        freq[c].append(n)
    
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]: 
            res.append(n)
            if len(res) == k: 
                return res   
