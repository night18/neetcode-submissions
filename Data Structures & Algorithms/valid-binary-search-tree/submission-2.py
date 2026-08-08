# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # To check validity, we need to check the max on the left tree and the min on the right tree.

        def _is_valid(node):
            # return valid, min, max
            if not node:
                # Null Node is valid
                return True, float("inf"), float("-inf")

            if node.left:
                l_v, l_min, l_max = _is_valid(node.left)
            else:
                l_v, l_min, l_max = True,  float("inf"), float("-inf")

            if node.right:
                r_v, r_min, r_max = _is_valid(node.right)
            else:
                r_v, r_min, r_max = True,  float("inf"), float("-inf")
            if l_v and r_v:
                return node.val > l_max and node.val < r_min, min(l_min, node.val), max(r_max, node.val)

            else:
                # One sub tree is not valid
                return False, None, None
        
        return _is_valid(root)[0]

            