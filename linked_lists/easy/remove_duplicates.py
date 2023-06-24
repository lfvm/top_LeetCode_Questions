"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


Input: head = [1,1,2]
Output: [1,2]

https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/


"""

class Solution1(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        #O(n) time and O(n) space 
        values = set()
        result = None
        current = None
        while head: 

            if head.val in values:
                head = head.next
                continue 

            newNode = ListNode(head.val)
            if not result:
                result = newNode
                current = result
            else:
                current.next = newNode
                current = current.next
    
            values.add(head.val)
            head = head.next

        return result
    

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #O(n) time O(1) space
        temp = head
        while (temp and temp.next):
            # same repeated values
            if (temp.next.val == temp.val):
                temp.next = temp.next.next
                continue

            temp = temp.next
        return head
    