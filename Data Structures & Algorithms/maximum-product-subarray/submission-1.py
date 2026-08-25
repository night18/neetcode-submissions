class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]

        pre = post = 0

        for i in range(n):
            pre = nums[i] * (pre or 1) # To avoid starter or truncate with 0
            post = nums[n-1-i] * (post or 1)

            result = max(result, max(pre, post))
        return result