from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    q.append((x,y,0))
                    grid[x][y] == -1

        counter = 0
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]

        while q:
            x, y, t = q.popleft()

            for dx, dy in directions:
                if (
                    x+dx >= 0 and
                    y+dy >= 0 and
                    x+dx < len(grid) and 
                    y+dy < len(grid[0]) and 
                    grid[x+dx][y+dy] == 1):
                        grid[x+dx][y+dy] = -1
                        q.append((x+dx, y+dy, t+1))
                        counter = max(counter, t+1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    return -1

        return counter

