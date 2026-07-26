class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i, num in enumerate(nums):
            if num in my_map:
                return [my_map[num], i]
            my_map[target-num] = i
        return [0,0]