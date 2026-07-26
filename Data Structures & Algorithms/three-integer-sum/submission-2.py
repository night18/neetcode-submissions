from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        my_map = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] <= nums[j]:
                    my_map[0 - (nums[i] + nums[j])].append([i, j])
                else:
                    my_map[0 - (nums[i] + nums[j])].append([j, i])

        results = set()
        for i in range(len(nums)):
            if nums[i] in my_map:
                for j, k in my_map[nums[i]]:
                    if i != j and i != k:
                        if nums[i] <= nums[j]:
                            results.add(tuple([nums[i], nums[j], nums[k]]))
                        elif nums[i] <= nums[k]:
                            results.add(tuple([nums[j], nums[i], nums[k]]))
                        else:
                            results.add(tuple([nums[j], nums[k], nums[i]]))

        return [list(sub_tuple) for sub_tuple in results]