# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def _is_good(self, node, max_parent):
            
            if node:
                if node.val >= max_parent: # >= because no grater than
                    self.count += 1

                _is_good(self, node.left, max(max_parent, node.val) )
                _is_good(self, node.right, max(max_parent, node.val) )
        
        _is_good(self, root, float("-inf"))

        return self.count