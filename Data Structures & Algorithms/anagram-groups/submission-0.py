from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list) 

        for string in strs:
            local_set = Counter(string)
            local_set_string = str(sorted( local_set.items(), key=lambda item: (-item[1], item[0])))
            
            output[local_set_string].append(string)
            
        return [x for x in output.values()]