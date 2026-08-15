from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    q = deque([(i, j)])
                    visited = set()
                    is_alive = False

                    while q:
                        x, y = q.popleft()
                        if (x, y) in visited:
                            continue
                        visited.add((x, y))
                        if x == 0 or x == len(board) - 1 or y == 0 or y == len(board[0]) - 1:
                            is_alive = True
                            break
                        
                        for dx, dy in directions:
                            if x + dx >= 0 and x + dx < len(board) and y + dy >= 0 and y + dy < len(board[0]) and board[x+dx][y+dy] == "O":
                                q.append((x+dx, y+dy))

                    if not is_alive:
                        for x, y in visited:
                            board[x][y] = "X" 

