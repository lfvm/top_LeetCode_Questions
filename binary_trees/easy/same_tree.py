"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Input: p = [1,2,3], q = [1,2,3]
Output: true

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
            
def isSameTree( p , q) -> bool:
        
    list1 = bfs(p)
    list2 = bfs(q)
    
    return list1 == list2



def bfs(root):
    queue = []
    result = []
    queue.append(root)
    
    while len(queue) > 0:
        
        element = queue.pop(0)

        if element is None:
            result.append(element)
            continue
        
        queue.append(element.right)
        queue.append(element.left)
        result.append(element.val)

    return result



        
"""
Solucion:

Iterar el arbol utilizando breath first search y guardar sus valores en una lista.

Si las listas son iguales regresar true si no false
"""