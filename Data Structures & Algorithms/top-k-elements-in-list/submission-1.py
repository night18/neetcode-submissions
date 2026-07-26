class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)          # 用「次數」當索引

        res = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res