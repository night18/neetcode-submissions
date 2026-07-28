class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        day = 0
        result = [0]*len(temperatures)
        
        
        q = []

        for i, t in enumerate(temperatures):

            while len(q)> 0 and q[-1][0] < t:
                pt, pi = q.pop()
                result[pi] = i - pi

            q.append((t, i))

        while q:
            pt, pi = q.pop()
            result[pi] = 0

        return result

            

            

            
        


        

        

            

            

