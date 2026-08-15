from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Impossible means the no rotten fruits or rotten fruits would not affect frsh fruits
        
        minutes = 0
        directions = [(1, 0), (0, 1), (-1,0), (0, -1)]
        visited = set()
        q = deque([])
        # Find the rotten fruit first
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            x, y, m = q.popleft()
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and (x,y) not in visited and grid[x][y] > 0:
                visited.add((x, y))
                if grid[x][y] == 1: #fresh fruit
                    minutes = max(minutes, m)
                    grid[x][y] = 2

                for dx, dy in directions:
                    q.append((x+dx, y+dy, m+1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return minutes