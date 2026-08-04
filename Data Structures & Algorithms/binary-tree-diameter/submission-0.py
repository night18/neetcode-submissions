# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def length_and_depth(node):
            if node is None:
                return 0, 0

            left_length, left_depth = length_and_depth(node.left)
            right_length, right_depth = length_and_depth(node.right)

            return max( left_depth+ right_depth, left_length, right_length), 1+ max(left_depth, right_depth)
        return length_and_depth(root)[0]