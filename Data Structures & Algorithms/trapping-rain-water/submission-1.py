class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        if len(height) < 3:
            return 0

        left = [0] * len(height)
        right = [0] * len(height)

        left[0] = height[0]
        for i in range(1, len(height) - 1):
            left[i] = max(left[i-1], height[i])

        right[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, 0, -1):
            right[i] = max(right[i+1], height[i])


        for i in range(i, len(height) - 1):
            water += max(min(left[i], right[i]) - height[i], 0)


        return water