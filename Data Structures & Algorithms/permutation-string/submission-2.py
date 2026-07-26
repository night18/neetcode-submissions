class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        base = [0] * 26
        for i in range(len(s1)):
            base[ ord(s1[i]) - ord("a") ] += 1

        t_base = tuple(base) 
        counter = [0] * 26

        for i in range(len(s2)):
            counter[ ord(s2[i]) - ord("a") ] += 1

            if i >= len(s1):
                counter[ ord(s2[i-len(s1)]) - ord("a") ] -= 1
            
            if t_base == tuple(counter):
                return True

        return False
    
