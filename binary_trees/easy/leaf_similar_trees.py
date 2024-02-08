"""
872. Leaf-Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isLeaf(self,node):
        return node.left is None and node.right is None


    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        leafs1 = []
        leafs2 = []


        def preorder(root, lst):

            if not root:
                return
            
            if self.isLeaf(root):
                lst.append(root.val)
         
            preorder(root.left,lst)
            preorder(root.right,lst)


        preorder(root1,leafs1)
        preorder(root2,leafs2)

        return leafs1 == leafs2