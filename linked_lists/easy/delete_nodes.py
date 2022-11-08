"""
Remove linked list elements
https://leetcode.com/problems/remove-linked-list-elements/


Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head , val: int):
        
    #Una cabeza que nos ayudara en caso de que el primer nodo 
    #Sea el valor que queremos eliminar
    toolHead = ListNode(-1)
    toolHead.next = head
    current = toolHead 
    
    while current:
        
        nextNode = current.next 
    
        if nextNode and nextNode.val == val:
            current.next = nextNode.next
        else:
            current = nextNode
            
        
    
    return toolHead.next
                