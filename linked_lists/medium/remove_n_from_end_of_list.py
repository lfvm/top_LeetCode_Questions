"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


Input: head = [1], n = 1
Output: []

"""

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
    
        dummy = ListNode() 
        dummy.next = head 
        slow = dummy 
        fast = head


        
        if not fast:
            return head.next

        while fast:
            slow = slow.next 
            fast = fast.next

        slow.next = slow.next.next

        #return the head
        return dummy.next    



"""
Explanation:
two pointer approach:

If we advance the fast pointer n times, we make sure that the distance between slow and fast is always n.
How does this help?


If we advance fast n times: 

[1,2,3,4,5] n : 2
slow = 1 
fast = 3 


after that we continue iterating until fast is null, in that cas 

[1,2,3,4,5] n : 2
slow = 4 
fast = None

notice how slow is exactly the node we need to remove, the problem is that we have lost reference to the previous node and thus cant delete 4.


To solve that we create a dummy and asign slow to that dummy:

[dummy,1,2,3,4,5] n : 2
slow = dummy
fast = 3

when we end iterating slow is going to be one node behind the one we want to delete, we can just update pointers and thats it 
"""