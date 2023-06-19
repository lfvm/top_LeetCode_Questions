"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

"""


class Solution:
    def hasCycle(self, head) -> bool:
        
        slow = head        
        fast = head
    
        while True:
             
            if not fast:
                return False
            
            slow = slow.next 
            fast = fast.next
            
            if fast:
                fast = fast.next
            
            if slow == fast and fast and slow:
                return True
            

    def hasCycle2(self,head) -> bool:

        slow = head
        fast =  head 

        while (fast and fast.next):
            slow = slow.next 
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False


    def hasCycle3(self, head) -> bool:
        visited = set()
        current = head
        while True:
            
            if not current:
                return False
            
            if current in visited: 
                return True 
            
            visited.add(current)
            current = current.next

"""
Solucion 1:

Si utilizamos dos pointers, uno que recorre la lista de manera normal y otro que lo hace 
de dos en dos nodos, encontraremos dos casos, 1 que el pointer rapido llegue al final de la lista 
por lo tanto no hay ciclo o 2 eventualmente los pointers se encontraran nuevamente si existe 
un ciclo en la lista 

Solucion 2:

utlizar un set y guardar los nodos mientras se recorre la lista,
si se encuentra un nodo repetido quiere decir que existe un ciclo
"""