"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        clones = {node: Node(node.val)}
        q = deque([node])
        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n not in clones:
                    clones[n] = Node(n.val)   # 建 clone = 標記,發生在 enqueue 時
                    q.append(n)
                clones[cur].neighbors.append(clones[n])
        return clones[node]


        