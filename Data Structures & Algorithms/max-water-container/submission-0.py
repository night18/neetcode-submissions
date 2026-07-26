class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        contain = 0

        while l < r:
            contain = max(min(heights[l], heights[r]) * (r - l), contain)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return contain

            
