from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # from top left corner and use bfs for land
        island_count = 0
        is_traveled = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        moves = [(1,0), (0,1), (-1,0), (0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not is_traveled[i][j]:
                    is_traveled[i][j] = True
                    if grid[i][j] == "1":
                        island_count += 1
                        queue = deque([(i+1, j), (i, j+1), (i-1, j), (i-1, j)])
                        while queue:
                            curr = queue.popleft()
                            x, y = curr
                            if x > -1 and x < len(grid) and y > -1 and y < len(grid[0]) and not is_traveled[curr[0]][curr[1]]:
                            
                                is_traveled[curr[0]][curr[1]] = True
                                if grid[curr[0]][curr[1]] == "1":
                                    queue.append((curr[0] + 1, curr[1]))
                                    queue.append((curr[0], curr[1] + 1))
                                    queue.append((curr[0] - 1, curr[1]))
                                    queue.append((curr[0], curr[1] - 1))

        return island_count



                    

