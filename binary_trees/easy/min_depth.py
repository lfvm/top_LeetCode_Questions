"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

"""




class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root: 
            return 0 

        if not root.left and not root.right: 
            return 1 
        
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        if not root.right:
            return 1 + self.minDepth(root.left)

        return min(1 + self.minDepth(root.left), 1 + self.minDepth(root.right))
