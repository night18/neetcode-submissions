# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 找深,樹形不確定，勢必每個都要經
        

        def depth(node, parent_depth):
            if node is None:
                return parent_depth

            return max(depth(node.left, parent_depth + 1), depth(node.right, parent_depth + 1))
        return depth(root, 0)







        