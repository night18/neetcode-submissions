class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brutal Force
        # return min(nums)
        
        # 1. The range of nums value can be large.
        # 2. Try to find the rotate time k
        # 3. Then nums[k % len(nums)] is the smallest.
        # 4. The problem is how to find the k.
        # 5. It can be binary search, but how to create the validator.
        # 6. Check whether the nums[k+1] < nums[k]. If yes, then k is right.

        def valid(nums, t):
            return nums[0] > nums[t]

        l = 0
        r = len(nums)
        t = 0

        while l <= r:
            m = (l + r) // 2
            if m < len(nums) and valid(nums, m):
                t = m
                r = m -1
            else:
                l = m + 1
                
        return nums[t]