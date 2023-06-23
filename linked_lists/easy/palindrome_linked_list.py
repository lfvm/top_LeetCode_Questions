"""
234. Palindrome Linked List


Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
"""

class Solution(object):

    #Approach one is O(n) time and O(n) space beacuse it uses an array
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        tempArray = []
        while head: 
            tempArray.append(head.val)
            head = head.next 
        
        left = 0
        right = len(tempArray) - 1

        while right > left: 

            if tempArray[left] != tempArray[right]:
                return False

            left += 1
            right -= 1

        return True  
    



class Solution2(object):

    # Aproach to O(n) time and O(1) space.
    #Consists on getting the middle of the linked list, and reversing that midle
    def reverse(self,head):

        prev = None 
        current = head 
        while current:
            temp = current.next 
            current.next = prev 
            prev = current 
            current = temp
        
        return prev 

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast, slow = head, head

        #find the middle of the array (slow) 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next

        #reverse second half
        right = self.reverse(slow)
        left = head

        #Compare values from left to right and check if they match
        while right and left: 
            if right.val != left.val:
                return False

            left = left.next
            right = right.next

        return True
