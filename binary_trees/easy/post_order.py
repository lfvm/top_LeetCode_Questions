"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

https://leetcode.com/problems/binary-tree-postorder-traversal/description/

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        def postorder(root):

            if not root:
                return
            
            postorder(root.left)
            postorder(root.right)

            result.append(root.val)

        postorder(root)

        return result