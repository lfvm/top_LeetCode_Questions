"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

https://leetcode.com/problems/add-two-numbers/description/

"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
  
        current = None
        carry = 0 
        head = None

        while l1 or l2:
            currentSum = carry
            
            if l1: 
                currentSum += l1.val 
                l1 = l1.next
            
            if l2: 
                currentSum += l2.val 
                l2 = l2.next
 
            # we use the % in case the sum is grater than 10 example: 14 % 10 = 4;   6 % 10 = 6
            node = ListNode(currentSum % 10)

            carry = currentSum / 10
            # Or also valid: 
            # if currentSum >= 10:
            #     carry = 1
            # else: 
            #     carry = 0


            if not current:
                head = node
                current = node
            else:
                current.next = node 
                current = current.next
        if carry > 0:
            current.next = ListNode(1)

        return head
    