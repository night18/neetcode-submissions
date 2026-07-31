class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]*len(nums)

        
        for num in nums[:len(nums)-1]:
            left.append(left[-1] * num)
        
        for i in range(len(nums)-1, 0, -1): # exclude 0 in purpose.
            right[i-1] = right[i] * nums[i]

        return [left[i] * right[i] for i in range(len(nums))]
