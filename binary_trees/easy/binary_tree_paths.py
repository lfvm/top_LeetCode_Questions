"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

        1
      /   \
      2   3
      \
        5

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Input: root = [1]
Output: ["1"]


https://leetcode.com/problems/binary-tree-paths/description/

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
      
      ans = []
      def preorder(root,s):
        
        if not root: return
        
        s += str(root.val)


        if not root.right and not root.left:
          ans.append(s)
          return

        preorder(root.left, s+"->")
        preorder(root.right, s+"->")
        


      preorder(root,"")

      return ans