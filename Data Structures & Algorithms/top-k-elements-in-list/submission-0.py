from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        return [x[0] for x in sorted(Counter(nums).items(), key=lambda item: -item[1])][:k]
        