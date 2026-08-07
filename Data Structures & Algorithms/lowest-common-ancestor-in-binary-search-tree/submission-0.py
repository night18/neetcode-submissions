# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def is_child(node, p1, p2):
            if node:
                l_found_p1, l_found_p2, l_found = is_child(node.left, p1, p2)
                r_found_p1, r_found_p2, r_found = is_child(node.right, p1, p2)

                if l_found:
                    return True, True, l_found

                if r_found:
                    return True, True, r_found

                found_p1 = l_found_p1 or r_found_p1 or node.val == p1.val
                found_p2 = l_found_p2 or r_found_p2 or node.val == p2.val

                if found_p1 and found_p2:
                    return True, True, node

                return found_p1, found_p2, None
            else:
                return False, False, None

        return is_child(root, p, q)[2]