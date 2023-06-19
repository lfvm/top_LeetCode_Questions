"""
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

https://leetcode.com/problems/subtree-of-another-tree/
"""

class Solution(object):

    def isSameTree(self,p,q):
        
        # It is considerd same trees if both are null
        if not p and not q:
            return True 
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root and not subRoot: 
            return True

        queue = [ root ]

        result = False
        while len(queue) > 0:
            #BFS or DFS to find the node where it is possible to have a subtree

            node = queue.pop(0)

            if not node:
                continue

            if node.val == subRoot.val:
                result =  self.isSameTree(node,subRoot)

                if result == True:
                    return result

            queue.append(node.left)
            queue.append(node.right)


        return result