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
        
        #### Alternative Solution #####
        # set removes the duplicate 
        # the sum of nums - the sum of nums-1 divided the len(nums) - len(nums-1) will give the duplicate value 
        # nums = [1,3,4,2,2]
        # nums_updated = (1,3,4,2)
        # sum(nums) - sum(nums_updated) = 2 
        # len(nums) - len(nums_updated) = 1 
        # 2/1 = 2 which is the duplicate number 
        ######
        
        # nums_updated = set(nums)

        # return (sum(nums) - sum(nums_updated)) / (len(nums) - len(nums_updated))
            

    