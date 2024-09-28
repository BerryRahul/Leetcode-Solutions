def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the first point of intersection 
        slow, fast = 0, 0 
        while True: 
                slow = nums[slow]
                fast = nums[nums[fast]] # this moves twice as fast 
                if slow == fast: 
                        break 
        # after first point of intersection leave slow as is 
        # slow2 will be used to find the second point of intersection 
        # due to the preconditions of this problem the second 
        # point of intersection will always be the duplicate (floyds)
        slow2 = 0
        while True: 
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: 
                   return slow 