def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0 
        while True: 
                slow = nums[slow]
                fast = nums[nums[fast]] # this moves twice as fast 
                if slow == fast: 
                        break 
        slow2 = 0
        while True: 
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: 
                   return slow 