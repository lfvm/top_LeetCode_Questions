"""
Given the root of a binary tree, invert the tree, and return its root.

link: https://leetcode.com/problems/invert-binary-tree/

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTreeQueue( root ):
    
    #Breath first search 
    queue = []
    current = root 
    queue.append(current)
    
    
    while len(queue) != 0:
        
        tempNode = queue.pop(0)
        if tempNode: 
            
            #Meter los elementos a la cola 
            queue.append(tempNode.left)
            queue.append(tempNode.right)
            
            #Invertir los elementos
            tempLeft = tempNode.left
            tempNode.left = tempNode.right
            tempNode.right = tempLeft
    
    return root

def invertTreeStack( root ):
    
    #Depth first search 
    stack = []
    current = root 
    stack.append(current)
    
    
    while len(stack) != 0:
        
        tempNode = stack.pop()
        if tempNode: 
            
            #Meter los elementos a la cola 
            stack.append(tempNode.left)
            stack.append(tempNode.right)
            
            #Invertir los elementos
            tempLeft = tempNode.left
            tempNode.left = tempNode.right
            tempNode.right = tempLeft
    
    return root



"""
Solucion:

Realizar un recorrido del arbol ya sea con Depht first search o breath first search 
ir cambiando los elementos de lugar con cada nodo al mismo tiempo que se recorre
"""