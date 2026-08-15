from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        pre_map = [[] for _ in range(numCourses)]

        for dest, preq in prerequisites:
            in_degree[dest] += 1
            pre_map[preq].append(dest)

        q = deque()

        for idx, degree in enumerate(in_degree):
            if degree == 0:
                q.append(idx)


        seq = []
        
        while q:
            node = q.popleft()
            seq.append(node)

            for next_course in pre_map[node]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)
        
        if len(seq) != numCourses:
            return []
        print(seq)
        return seq