class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = [nums[0]]
        passed = [0]
        n = len(nums)

        for i in range(1, n):
            robbed.append(passed[i-1] + nums [i])
            passed.append(max(robbed[i-1], passed[i-1]))

            # print(i)
            # print(robbed)
            # print(passed)
        
        return max(robbed[n-1], passed[n-1])