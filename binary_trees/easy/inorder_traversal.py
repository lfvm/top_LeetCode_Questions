"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
https://leetcode.com/problems/binary-tree-inorder-traversal/

Input: root = [1,null,2,3]
Output: [1,3,2]

"""



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
        
    stack = []
    result =[]
    current = root
    while True:
        
        #ir a la parte de hasta la izquierda del arbol  
        if current:
            
            stack.append(current)
            current = current.left
        #Llegamos al fondo de la parte izquierda del arbol 
        else:
            if len(stack) > 0:
                current = stack.pop()
                result.append(current.val)
                current = current.right
                
            #Si ya no hay elementos en el stack salir del loop 
            else:
                break
                
    return result
            