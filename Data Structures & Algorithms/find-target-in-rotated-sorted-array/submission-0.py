class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Same as the last Q, find the T turns first.

        def valid(nums, t):
            return nums[0] > nums[t]

        l = 0
        r = len(nums) - 1 
        t = 0

        while l <= r:
            m = (l + r) // 2
            if valid(nums, m):
                t = m
                r = m - 1
            else:
                l = m + 1

        # The most easy way is to rebuild the list with the rotate.
        # But it might require O(n) to process that

        l = 0
        r = len(nums) - 1 

        if target >= nums[t] and target <= nums[r]:
            # right part
            l = t
        else:
            r = t - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1


        return -1
