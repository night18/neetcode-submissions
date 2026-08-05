# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result

        stack = deque([(root, 0)])
        
        layer_list = []
        layer_depth = 0

        while stack:
            curr_node, curr_layer = stack.popleft()

            if curr_layer > layer_depth:
                result.append(layer_list)
                layer_list = []
                layer_depth=curr_layer

            if curr_node:
                layer_list.append(curr_node.val)
                stack.append((curr_node.left, curr_layer + 1))
                stack.append((curr_node.right, curr_layer + 1))


        return result
        