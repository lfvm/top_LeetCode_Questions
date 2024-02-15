"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

https://leetcode.com/problems/binary-tree-right-side-view/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
      result = []
      q = []
      q.append(root)

      while q:

          rightMostNode = None

          for i in range(len(q)):

              node = q.pop(0)

              if node:
                  q.append(node.left)
                  q.append(node.right)
                  rightMostNode = node 

          if rightMostNode:
              result.append(rightMostNode.val)


      return result 


        