"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.


https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def doInsert(self,root,val):
        
        if val < root.val:

            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)

        else:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)

    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
    
        if not root: 
            return TreeNode(val)

        self.doInsert(root,val)
        return root
       