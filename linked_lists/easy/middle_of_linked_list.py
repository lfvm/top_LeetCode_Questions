"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode( head ):
        
    result = head
    fast = head 
    
    while fast:
        if fast == None or fast.next == None:
            return result
        
        result = result.next
        fast = fast.next.next
        
    return result


"""
Solucion:

Tener un apuntador que recorre la lista normalmente y un apuntador que se mueve de dos nodos en dos nodos.

Cuando el segundo apuntador llegue al final, el primero se encontrara en el centro.

"""