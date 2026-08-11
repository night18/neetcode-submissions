from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_island = 0
        is_traveled = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not is_traveled[i][j]:
                    is_traveled[i][j] = True
                    if grid[i][j] == 1:
                        local_island = 1
                        queue = deque([(i+1, j), (i, j+1), (i-1, j), (i, j-1)])
                        while queue:
                            curr = queue.popleft()
                            x, y = curr
                            if x > -1 and x < len(grid) and y > -1 and y < len(grid[0]) and not is_traveled[x][y]:
                                is_traveled[x][y] = True
                                if grid[x][y] == 1:
                                    local_island += 1
                                    queue.append((x + 1, y))
                                    queue.append((x, y + 1))
                                    queue.append((x - 1, y))
                                    queue.append((x, y - 1))

                        max_island = max(max_island, local_island)

        return max_island
