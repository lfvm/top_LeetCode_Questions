"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


class Solution(object):


    #DFS becasuse we need to go from the top to the bottom 
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []  

        result = []
        queue = [ root ]

        while len(queue) > 0:
            
            level = []

            for i in range(len(queue)):
                element = queue.pop(0)
                if element:
                    level.append(element.val)
                    queue.append(element.left)
                    queue.append(element.right)
      
            if level:
                result.append(level)

        return result
            

