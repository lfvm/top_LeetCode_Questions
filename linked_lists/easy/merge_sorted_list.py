"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def mergeTwoLists(list1, list2):
        
    result = ListNode(0)
    temp = result
    
    while (list1 and list2):
        
        #Mientras podamos iterar ambas listas 
        
        if list1.val <= list2.val:
            temp.next = list1
            temp = list1
            list1 = list1.next 
            
        else:
            temp.next = list2 
            temp = list2
            list2 = list2.next 
        
        
    # En caso de que hayan sobrado elementos en cualquiera de las listas, agregar lo que falta 
    # al resulado
        
    if list1:
        temp.next = list1
    else: 
        temp.next = list2
    
    return result.next
        
