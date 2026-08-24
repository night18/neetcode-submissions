class Solution:
    def rob(self, nums: List[int]) -> int:
        first_robbed = [nums[0]]
        first_not_robbed = [0]
        n = len(nums)

        for i in range(1, n):
            if i == 1:
                first_robbed.append(nums[0])
                first_not_robbed.append(nums[1])
            elif i == n-1:
                first_robbed.append(first_robbed[i-1])
                first_not_robbed.append(max(first_not_robbed[i-1], first_not_robbed[i-2] + nums[i]))
            else:
                first_robbed.append(max(first_robbed[i-1], first_robbed[i-2] + nums[i]))
                first_not_robbed.append(max(first_not_robbed[i-1], first_not_robbed[i-2] + nums[i]))


        return max(first_robbed[n-1], first_robbed[n-2], first_not_robbed[n-1], first_not_robbed[n-2])