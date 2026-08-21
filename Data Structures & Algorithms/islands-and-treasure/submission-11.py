from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Start with treasure
        q = deque()
        traveled = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
                    traveled.add((i, j))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            x, y, dist = q.popleft()
            if dist > grid[x][y]:
                continue
            grid[x][y] = dist
            # print(grid)

            for dx, dy in directions:
                if min(x+dx, y+dy) < 0 or x+dx >= len(grid) or y+dy>=len(grid[0]) or (x+dx, y+dy) in traveled or dist+1 >= grid[x+dx][y+dy]:
                    continue
                
                q.append((x+dx, y+dy, dist+1))
                traveled.add((x+dx, y+dy))

