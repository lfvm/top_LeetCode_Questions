"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

"""


def searchBST(root, val: int):
           
    if root is None:
        return None
    
    if root.val == val:
        return root
    
    if root.val > val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)


"""
    Solucion recursiva:

    casos base:
        - Root es None (no se encontro el valor)
        - Root es igual al valor (se encontro la solucion)

    Iteracion:

        Si el valor a buscar es mayor al root entonces iterar en el arbol de la derecha
        de lo contrario ir a la izquierda
"""