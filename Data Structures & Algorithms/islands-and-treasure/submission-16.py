from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Start with treasure
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                if min(x+dx, y+dy) < 0 or x+dx >= len(grid) or y+dy>=len(grid[0]) or grid[x+dx][y+dy] != 2147483647:
                    continue
                
                q.append((x+dx, y+dy))
                grid[x+dx][y+dy] = grid[x][y] + 1
                
