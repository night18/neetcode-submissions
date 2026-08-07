# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def _balance(node):
            if not node:
                return 0, True
            
            l_depth, l_balnce = _balance(node.left)
            r_depth, r_balnce = _balance(node.right)

            return max(l_depth, r_depth) + 1, abs(l_depth-r_depth) < 2 and l_balnce and r_balnce

        return _balance(root)[1]