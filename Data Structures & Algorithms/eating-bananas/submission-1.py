import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Because it wants to find the minimum integer k.
        # We need to start the k (per hour eating rate) from 1.
        # And find the first valid one. 
        # It is a binary search question. How to search that?
        def valid(piles, k, h):
            return sum([ math.ceil(pile/k) for pile in piles]) <= h

        l = 1
        r = max(piles)
        valid_index = -1

        while l <= r:
            m = ( l + r ) // 2
            is_valid = valid(piles, m, h)
            
            if is_valid:
                valid_index = m
                r = m - 1
            else:
                l = m + 1

        return valid_index

