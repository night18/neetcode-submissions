from collections import defaultdict
import heapq
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.time_map[key], (timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        temp_list = self.time_map[key]
        l, r = 0, len(temp_list) - 1
        result = ""

        while l <= r:
            m = (l + r) // 2

            if temp_list[m][0] <= timestamp:
                result = temp_list[m][1]
                l = m + 1

            if temp_list[m][0] > timestamp:
                r = m - 1
                
        
        return result